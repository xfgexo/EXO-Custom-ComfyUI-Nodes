# 
# ComfyUI_EXO_FluxSampler.py
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
EXO FluxSampler 👑
-----------------------------
The ComfyUI EXO FluxSampler node is an advanced sampling node designed for ComfyUI. It provides flexible and customizable sampling capabilities, allowing for precise control over model sampling.

Features:
- Customizable Sampling: Including noise seed, increment value, sampler name, scheduler, and more.
- Model Sampling: Utilizes a custom ModelSamplingFlux logic.
- Noise Generation: Includes a built-in noise generator.
- Guidance Integration: Supports conditioning guidance.

Inputs:
- Model: The model to be used for sampling.
- Conditioning: The conditioning tensor for guiding the sampling process.
- Width and Height: Dimensions for the output image.
- Noise_Seed: Seed for noise generation, ensuring reproducibility.
- Increment_Value: Increment value for sampling adjustments.
- Sampler_Name: Chooses the sampler algorithm.
- Scheduler: Selects the scheduling method for sigma generation.
- Steps: Number of steps for the sampling process.
- Denoise: Denoising factor for adjusting the sampling intensity.
- Max_Shift and Base_Shift: Parameters for controlling the sampling shift.
- Guidance: Guidance factor for conditioning adjustments.
- Negative_Conditioning (optional): Additional conditioning for negative guidance.

Outputs:
- Model_Out: The processed model with applied sampling.
- Noise: The generated noise object.
- Sampler: The sampler object used for processing.
- Sigmas: The computed sigmas for the sampling process.
- Seed: The seed dictionary for noise generation.
- Latent: The generated latent image tensor.
- Guider: The guidance object for conditioning.
- Conditioning_Out: The adjusted conditioning tensor with applied guidance.
"""

import comfy.samplers
import torch
import comfy.sample
import random
import comfy.model_sampling
import node_helpers
from nodes import EmptyLatentImage

class ComfyUI_EXO_FluxSampler:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model": ("MODEL", {"tooltip": "Connect this to a node that has a model output."}),
                "pos_cond_in": ("CONDITIONING", {"tooltip": "Connect this to a node that has a positive conditioning output."}),
                "width": ("INT", {"forceInput": True, "tooltip": "Connect this to a node that has an image width output."}),
                "height": ("INT", {"forceInput": True, "tooltip": "Connect this to a node that has an image height output."}),
                # NOISE section
                "noise_seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                "increment_value": ("INT", {"default": 1, "min": 1, "max": 10000, "step": 1}),
                # SAMPLER section
                "sampler_name": (comfy.samplers.SAMPLER_NAMES,),
                # SCHEDULER section
                "scheduler": (comfy.samplers.SCHEDULER_NAMES,),
                "steps": ("INT", {"default": 20, "min": 1, "max": 10000}),
                "denoise": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.01}),
                # Additional parameters
                "max_shift": ("FLOAT", {"default": 0.70, "min": 0.0, "max": 100.0, "step": 0.01}),
                "base_shift": ("FLOAT", {"default": 0.30, "min": 0.0, "max": 100.0, "step": 0.01}),
                "guidance": ("FLOAT", {"default": 2.0, "min": 0.0, "max": 100.0, "step": 0.1}),
            },
            "optional": {
                "neg_cond_in": ("CONDITIONING", {"tooltip": "Connect this to a negative conditioning input."}),
            }
        }
    
    OUTPUT_TOOLTIPS = (
        "Connect this model output to a node that has a model input.",
        "Connect this noise output to a node that has a noise input.",
        "Connect this sampler output to a node that has a sampler input.",
        "Connect this sigmas output to a node that has a sigmas input.",
        "Connect this seed output to a node that has a seed input.",
        "Connect this latent output to a node that has a latent input.",
        "Connect this guider output to a node that has a guider input.",
        "Connect this conditioning output to a node that has a positive conditioning input.",
        "Connect this conditioning output to a node that has a negative conditioning input."
    )
    RETURN_TYPES = ("MODEL", "NOISE", "SAMPLER", "SIGMAS", "SEED", "LATENT", "GUIDER", "CONDITIONING", "CONDITIONING")
    RETURN_NAMES = ("model_out", "noise", "sampler", "sigmas", "seed", "latent", "guider", "pos_cond_out", "neg_cond_out")
    FUNCTION = "generate"
    CATEGORY = "Custom EXO Nodes"

    def neg_out_cond(self, neg_cond_in):
        """
        Process negative conditioning.
        
        Args:
            neg_cond_in: The negative conditioning input.
        
        Returns:
            Processed negative conditioning.
        """
        # Example logic for processing negative conditioning
        processed_negative = node_helpers.conditioning_set_values(neg_cond_in, {"scale": 1.0})
        return processed_negative

    def generate(self, model, pos_cond_in, width, height, noise_seed, increment_value, 
                sampler_name, scheduler, steps, denoise, max_shift, base_shift, guidance,
                neg_cond_in=None):
        # Handle edge cases
        noise_seed = max(0, noise_seed)
        increment_value = max(1, increment_value)

        # Use provided negative conditioning or default to positive conditioning
        negative = neg_cond_in if neg_cond_in is not None else pos_cond_in

        # Model Sampling Flux logic
        m = model.clone()
        x1 = 256
        x2 = 4096
        mm = (max_shift - base_shift) / (x2 - x1)
        b = base_shift - mm * x1
        shift = (width * height / (8 * 8 * 2 * 2)) * mm + b

        # Set up model sampling
        sampling_base = comfy.model_sampling.ModelSamplingFlux
        sampling_type = comfy.model_sampling.CONST

        class ModelSamplingAdvanced(sampling_base, sampling_type):
            pass

        model_sampling = ModelSamplingAdvanced(model.model.model_config)
        model_sampling.set_parameters(shift=shift)
        m.add_object_patch("model_sampling", model_sampling)

        # Generate sigmas using scheduler
        total_steps = steps
        if denoise < 1.0:
            if denoise <= 0.0:
                sigmas = torch.FloatTensor([])
            else:
                total_steps = int(steps/denoise)
        
        sigmas = comfy.samplers.calculate_sigmas(
            model.get_model_object("model_sampling"), 
            scheduler, 
            total_steps
        ).cpu()
        
        if denoise < 1.0:
            sigmas = sigmas[-(steps + 1):]

        # Create sampler object
        sampler = comfy.samplers.sampler_object(sampler_name)

        # Create noise generator
        class NoiseGenerator:
            def __init__(self, seed):
                self.seed = seed
            
            def generate_noise(self, input_latent):
                latent_image = input_latent["samples"]
                batch_inds = input_latent["batch_index"] if "batch_index" in input_latent else None
                return comfy.sample.prepare_noise(latent_image, self.seed, batch_inds)

        noise = NoiseGenerator(noise_seed)

        # Create seed dictionary for SEED type output
        seed_dict = {"seed": noise_seed}

        # Create latent using EmptyLatentImage
        latent = EmptyLatentImage().generate(width, height, batch_size=1)[0]

        # Create basic guider
        class Guider_Basic(comfy.samplers.CFGGuider):
            def set_conds(self, positive):
                self.inner_set_conds({"positive": positive})

        guider = Guider_Basic(model)
        guider.set_conds(pos_cond_in)

        # Apply guidance to conditioning (from FluxGuidance)
        conditioning_out = node_helpers.conditioning_set_values(pos_cond_in, {"guidance": guidance})

        # Process negative conditioning
        neg_cond_out = self.neg_out_cond(neg_cond_in)

        # Return all outputs
        return (m, noise, sampler, sigmas, seed_dict, latent, guider, conditioning_out, neg_cond_out)

NODE_CLASS_MAPPINGS = {
    "ComfyUI_EXO_FluxSampler": ComfyUI_EXO_FluxSampler
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ComfyUI_EXO_FluxSampler": "ComfyUI EXO FluxSampler 👑"
}
