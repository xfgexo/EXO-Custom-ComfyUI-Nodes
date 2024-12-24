# 
# ComfyUI_EXO_ImageRescale.py
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License v3.0 as published
# by the Free Software Foundation.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# 
# The GPL license ensures that any derivative work based on GPL-licensed code
# must also be distributed under the same GPL license terms. This means that if
# you modify GPL-licensed software and distribute your modified version, you must
# also provide the source code and allow others to modify and distribute it under
# the same GPL license.
# 
# A copy of the GNU General Public License is included within these project files.
# 
# Date: Dec.17.2024
# Author: Joe Porter / AKA: xfgexo
# Contact: exo@xfgclan.com
# URL Link: https://github.com/xfgexo/EXO-Custom-ComfyUI-Nodes

"""
EXO Image Rescale Node 👑
-----------------------------
A versatile image rescaling node for ComfyUI that provides multiple scaling modes:

Modes:
- Ignore: Passes the image through without any modifications
- Resize: Resizes the image to specific width and height dimensions
- Upscale: Enlarges the image by a specified scale factor
- Downscale: Reduces the image by a specified scale factor

Features:
- Multiple resampling methods (lanczos, nearest, bilinear, bicubic)
- Supersampling anti-aliasing option for higher quality results
- Maintains proper tensor format for ComfyUI compatibility
- Configurable scale factors via external JSON configuration

Input Parameters:
- Image: Input image tensor
- Mode: Scaling mode selection
- Scale_Factor: Multiplier for upscale/downscale operations
- Resize_Width: Target width for resize mode
- Resize_Height: Target height for resize mode
- Resampling: Algorithm used for resizing
- Supersample: Anti-aliasing method selection
- Force_Resize: Option to force exact dimensions

Output:
- Processed image tensor in the correct format for ComfyUI (B,C,H,W)
"""

import torch
import numpy as np
from PIL import Image
from .functions import pil2tensor, tensor2pil, apply_rescale_image
import json
import os
import comfy.utils  # Add this import for the progress bar

# Load the config file
config_path = os.path.join(os.path.dirname(__file__), 'Scale_Factor_config.json')
try:
    with open(config_path, 'r') as file:
        scale_factors = json.load(file)
    # Extract scale values from the config
    scale_values = [entry["scale_value"] for entry in scale_factors]
except Exception as e:
    print(f"Warning: Could not load Scale_Factor_config.json: {str(e)}")
    scale_values = [2.0]  # Default fallback value


class ComfyUI_EXO_ImageRescale:

    @classmethod
    def INPUT_TYPES(s):
        resampling_methods = sorted(["Lanczos", "Nearest", "Bilinear", "Bicubic"])  # Sorted alphabetically
        modes = ["Ignore", "Upscale", "Downscale", "Resize"]

        return {
            "required": {
                                "Image": ("IMAGE", {
                    "tooltip": "Connect this to a node that has an image output."
                }),
                "Mode": (modes, {
                    "tooltip": "Ignore: No changes to image   Upscale: Enlarges image keeping aspect ratio   Downscale: Shrinks image keeping aspect ratio   Resize: Forces exact width and height dimensions"
                }),
                "Scale_Factor": (scale_values, {
                    "tooltip": "Values from Scale_Factor_config.json   Used in Upscale: multiplies size by factor   Used in Downscale: divides size by factor"
                }),
                "Resize_Width": ("INT", {
                    "default": 1024, 
                    "min": 1, 
                    "max": 8192, 
                    "step": 1,
                    "tooltip": "Target width in pixels   Only used when Mode is set to Resize"
                }),
                "Resize_Height": ("INT", {
                    "default": 1024, 
                    "min": 1, 
                    "max": 8192, 
                    "step": 1,
                    "tooltip": "Target height in pixels   Only used when Mode is set to Resize"
                }),
                "Resampling": (resampling_methods, {
                    "default": "Lanczos",
                    "tooltip": "Algorithm used for ALL resize operations:   Lanczos: High quality   Nearest: Fast   Bilinear: Smooth   Bicubic: Sharp"
                }),
                "Supersample": (["true", "false"], {
                    "tooltip": "When enabled: Upscales 8x first   Then downscales to target size   Uses selected Resampling method"
                }),
                "Force_Resize": (["disabled", "enabled"], {
                    "tooltip": "When enabled in Resize mode:   Forces exact dimensions   Ignores aspect ratio"
                })
            }
        }

    OUTPUT_TOOLTIPS = (
        "Connect this image output to a node that has an image input.",
    )

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("Image",)
    FUNCTION = "process_image"
    CATEGORY = "Custom EXO Nodes"

    def process_image(self, Image, Mode, Scale_Factor, Resize_Width, Resize_Height, Resampling, Supersample, Force_Resize):
        # If Mode is "Ignore", ensure proper tensor format
        if Mode == "Ignore":
            if len(Image.shape) == 3:
                Image = Image.unsqueeze(0)
            return (Image,)

        # Convert tensor to PIL image
        pil_img = tensor2pil(Image)
        original_width, original_height = pil_img.size

        # Initialize progress bar with more steps for better granularity
        # 2 steps for initial setup, 8 steps for supersample if enabled, 10 steps for final resize
        total_steps = 20
        if Supersample == "true":
            total_steps += 10  # Add more steps for supersampling

        if Mode == "Upscale":
            pbar = comfy.utils.ProgressBar(total_steps)
            # Update for initial setup
            pbar.update(2)
        else:
            pbar = None

        # Handle different modes
        if Mode == "Resize":
            new_width = Resize_Width
            new_height = Resize_Height
        elif Mode == "Upscale":
            new_width = int(original_width * float(Scale_Factor))
            new_height = int(original_height * float(Scale_Factor))
        elif Mode == "Downscale":
            new_width = int(original_width / float(Scale_Factor))
            new_height = int(original_height / float(Scale_Factor))
        else:
            raise ValueError(f"Invalid mode: {Mode}")

        # Ensure the new dimensions are valid
        new_width = max(1, new_width)
        new_height = max(1, new_height)

        # Apply the resize/rescale
        resized_image = apply_rescale_image(
            pil_img,
            original_width,
            original_height,
            rounding_modulus=8,
            mode=Mode,
            force_resize=Force_Resize == "enabled",
            factor=float(Scale_Factor) if Mode in ["Upscale", "Downscale"] else 1.0,
            width=new_width,
            height=new_height,
            resample=Resampling,
            supersample_aa=Supersample,
            progress_callback=pbar
        )

        # Convert PIL image back to tensor and ensure proper format
        image_tensor = pil2tensor(resized_image)
        
        # Ensure the tensor is in the correct format (B,C,H,W)
        if len(image_tensor.shape) == 3:
            image_tensor = image_tensor.unsqueeze(0)
        
        return (image_tensor,)


# Register node mappings
NODE_CLASS_MAPPINGS = {
    "ComfyUI_EXO_ImageRescale": ComfyUI_EXO_ImageRescale,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ComfyUI_EXO_ImageRescale": "ComfyUI EXO Image Rescale 👑"
}
