# 
# ComfyUI_EXO_FluxSampler_Mini.py
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
EXO FluxSampler Mini 👑
-----------------------------
The ComfyUI EXO FluxSampler Mini node is an sampling node designed for ComfyUI. It provides flexible sampling capabilities, allowing for control over model sampling.

Features:
- Model Sampling: Utilizes a custom ModelSamplingFlux logic.

Inputs:
- Model: The model to be used for sampling.
- Width and Height: Dimensions for the output image.
- Max_Shift: Parameters for controlling the sampling shift.
- Base_Shift: Parameters for controlling the sampling shift.

Outputs:
- Model_Out: The processed model with applied sampling.
"""


import nodes
import comfy.model_sampling

class ComfyUI_EXO_FluxSamplerMini:
    NAME = "ComfyUI EXO FluxSampler Mini 👑"
    CATEGORY = "Custom EXO Nodes"

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            "model": ("MODEL", {"tooltip": "Connect this to a node that has a model output."}),
            "width": ("INT", {"forceInput": True, "tooltip": "Connect this to a node that has an image width output."}),
            "height": ("INT", {"forceInput": True, "tooltip": "Connect this to a node that has an image height output."}),
            "max_shift": ("FLOAT", {
                "default": 1.15,
                "min": 0.0,
                "max": 100.0,
                "step": 0.01,
                "display": "number",
                "tooltip": "Specify the maximum shift value for sampling."
            }),
            "base_shift": ("FLOAT", {
                "default": 0.5,
                "min": 0.0,
                "max": 100.0,
                "step": 0.01,
                "display": "number",
                "tooltip": "Specify the base shift value for sampling."
            })
        }}

    RETURN_TYPES = ("MODEL",)
    OUTPUT_TOOLTIPS = ("Connect this model output to a node that has a model input.",)
    FUNCTION = "patch"

    def patch(self, model, width, height, max_shift, base_shift):
        """
        Patches the model with flux sampling parameters.
        
        Args:
            model: The input model to patch
            width: Image width from connected node
            height: Image height from connected node
            max_shift: Maximum shift value
            base_shift: Base shift value
        
        Returns:
            tuple: Contains the patched model
        """
        m = model.clone()

        # Constants from original implementation
        x1 = 256
        x2 = 4096
        
        # Calculate shift using the same formula as original
        mm = (max_shift - base_shift) / (x2 - x1)
        b = base_shift - mm * x1
        shift = (width * height / (8 * 8 * 2 * 2)) * mm + b

        # Set up the sampling classes
        sampling_base = comfy.model_sampling.ModelSamplingFlux
        sampling_type = comfy.model_sampling.CONST

        class ModelSamplingAdvanced(sampling_base, sampling_type):
            pass

        # Create and configure the model sampling
        model_sampling = ModelSamplingAdvanced(model.model.model_config)
        model_sampling.set_parameters(shift=shift)
        
        # Add the sampling patch to the model
        m.add_object_patch("model_sampling", model_sampling)
        
        return (m,)

# Node class and display name mappings
NODE_CLASS_MAPPINGS = {
    "ComfyUI_EXO_FluxSamplerMini": ComfyUI_EXO_FluxSamplerMini
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ComfyUI_EXO_FluxSamplerMini": "ComfyUI EXO FluxSampler Mini 👑"
}
