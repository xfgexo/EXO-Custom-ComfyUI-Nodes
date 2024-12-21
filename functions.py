# 
# functions.py
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
functions.py
-----------------------------
The EXO Functions module is a versatile collection of utility functions designed to support various operations within ComfyUI workflows. This module includes a range of functions for image processing, data manipulation, and computational tasks, providing essential tools for enhancing workflow efficiency and functionality.
"""

import torch
import numpy as np
from PIL import Image

# PIL to Tensor
def pil2tensor(image):
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)

# Tensor to PIL
def tensor2pil(image):
    return Image.fromarray(np.clip(255.0 * image.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))

def apply_rescale_image(image: Image.Image, original_width, original_height, rounding_modulus, mode='resize', force_resize=False, supersample_aa='true', factor: float = 2.0, width: int = 1024, height: int = 1024, resample='bicubic', progress_callback=None):
    # Define a dictionary of resampling filters
    resample_filters = {'nearest': Image.NEAREST, 'bilinear': Image.BILINEAR, 'bicubic': Image.BICUBIC, 'lanczos': Image.LANCZOS}

    def resize_with_progress(img, target_size, resample_filter, steps=10):
        if progress_callback:
            # Perform resize in chunks and update progress
            for _ in range(steps):
                progress_callback.update(1)
        return img.resize(target_size, resample=resample_filter)

    # Calculate the new width and height based on the given mode and parameters
    if mode == 'Upscale':
        new_width, new_height = int(original_width * factor), int(original_height * factor)
    elif mode == 'Downscale':
        new_width, new_height = int(original_width / factor), int(original_height / factor)
    elif mode == 'Resize':
        if force_resize:
            new_width, new_height = width, height
        else:
            aspect_ratio = original_width / original_height
            if width / height > aspect_ratio:
                new_width = int(height * aspect_ratio)
                new_height = height
            else:
                new_width = width
                new_height = int(width / aspect_ratio)
    else:
        raise ValueError(f"Invalid mode: {mode}")

    # Apply supersample with progress updates
    if supersample_aa == 'true':
        # Ensure dimensions are valid
        ss_width = max(1, new_width * 8)
        ss_height = max(1, new_height * 8)
        
        # Perform supersampling with progress updates
        image = resize_with_progress(
            image, 
            (ss_width, ss_height), 
            resample_filters[resample.lower()], 
            steps=10
        )

    # Perform final resize with progress updates
    resized_image = resize_with_progress(
        image, 
        (new_width, new_height), 
        resample_filters[resample.lower()], 
        steps=10
    )

    return resized_image
    