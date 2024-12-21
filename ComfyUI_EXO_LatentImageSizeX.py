# 
# ComfyUI_EXO_LatentImageSizeX.py
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
EXO Latent Image Size X 👑
-----------------------------
The ComfyUI EXO Latent Image Size X node is an enhanced version of the latent image size node within the ComfyUI framework. It allows for the generation of latent images with additional outputs for width and height, providing greater flexibility in workflow integration.

Features
- Dimension Selection: Offers a dropdown for selecting predefined dimensions.
- Batch Processing: Supports generating multiple images in a single batch.
- Additional Outputs: Provides separate outputs for the width and height of the selected dimensions.
- Configurable Defaults: Easily edit an external JSON configuration file, allowing for easy customization.
- Format: The format is "width x height (aspect ratio).

Inputs:
- Dimensions: A dropdown selection for choosing the desired dimensions of the latent image.
- Batch_Size: An integer input specifying the number of images to generate in a single batch.

Outputs:
- Latent: The generated latent image noise at the specified dimensions.
- Width: The width of the selected dimensions in pixels.
- Height: The height of the selected dimensions in pixels.
"""

import json
import os
from nodes import EmptyLatentImage

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Load the config file
config_path = os.path.join(script_dir, 'Latent_Image_Size_config.json')

with open(config_path, 'r') as file:
    config = json.load(file)

class ComfyUI_EXO_LatentImageSizeX:
    NAME = "ComfyUI_EXO_Latent Image Size X 👑"
    CATEGORY = "Custom EXO Nodes"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "dimensions": (
                    config["dimensions"],
                    {
                        "default": config["default"],
                        "tooltip": "Select the desired dimensions for your latent image. Format: width x height (aspect ratio)"
                    }),
                "batch_size": ("INT", {
                    "default": 1,
                    "min": 1,
                    "max": 64,
                    "tooltip": "Number of images to generate in a single batch. Higher values use more VRAM."
                }),
            },
        }

    RETURN_TYPES = ("LATENT", "INT", "INT")
    RETURN_NAMES = ("Latent", "Width", "Height")
    OUTPUT_TOOLTIPS = (
        "The latent image noise at the specified dimensions. Connect to nodes that process latent images.",
        "The width of the selected dimensions in pixels.",
        "The height of the selected dimensions in pixels."
    )
    FUNCTION = "generate"

    def generate(self, dimensions, batch_size):
        """
        Generates an empty latent image at the specified dimensions and batch size.
        Also returns the width and height as separate outputs.
        
        Args:
            dimensions (str): The dimensions string in format 'width x height (aspect ratio)'
            batch_size (int): Number of images to generate in batch
        
        Returns:
            tuple: Contains the generated latent image, width, and height
        """
        # Check if the selected item is a separator or space
        if dimensions.startswith('-----') or dimensions.strip() == "":
            raise ValueError("Please select a valid dimension setting, not a separator line")
            
        # Extract dimensions from the string (ignore the aspect ratio label in parentheses)
        dimensions_part = dimensions.split('(')[0].strip()
        result = [x.strip() for x in dimensions_part.split('x')]
        width = int(result[0])
        height = int(result[1])
        
        latent = EmptyLatentImage().generate(width, height, batch_size)[0]
        
        return (latent, width, height)

# Register node mappings
NODE_CLASS_MAPPINGS = {
    "ComfyUI_EXO_LatentImageSizeX": ComfyUI_EXO_LatentImageSizeX
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ComfyUI_EXO_LatentImageSizeX": "ComfyUI EXO Latent Image Size X 👑"
}
