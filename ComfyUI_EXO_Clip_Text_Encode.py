# 
# ComfyUI_EXO_Clip_Text_Encode.py
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
EXO Clip Text Encode 👑
-----------------------------

Features:
- Dual Prompt Handling: This node processes both positive and negative text prompts.
- Encoding: Utilizes CLIP models to convert text inputs into conditioning tensors.
- UTF-8 Compatibility: Ensures that text inputs are properly encoded in UTF-8.

Inputs:
- Clip_Input: Connect this to the output of a loaded CLIP model.
- Positive_Text: A multiline string input for positive prompts.
- Negative_Text: A multiline string input for negative prompts.

Outputs:
- Clip_Cond_Positive: The positive conditioning tensor.
- Clip_Cond_Negative: The negative conditioning tensor.
- Positive_Text: The original positive text prompt, available for downstream use.
- Negative_Text: The original negative text prompt, available for downstream use.
"""

class ComfyUI_EXO_Clip_Text_Encode:
    
    def __init__(self):
        self.type = "function"

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "Clip_Input": ("CLIP", {
                    "tooltip": "Connect this to a loaded CLIP model output."
                }),
                "Positive_Text": ("STRING", {
                    "multiline": True, 
                    "forceInput": True, 
                    "tooltip": "Connect this input to another nodes text (STRING) output."
                }),
                "Negative_Text": ("STRING", {
                    "multiline": True, 
                    "forceInput": True, 
                    "tooltip": "Connect this input to another nodes text (STRING) output."
                }),
            }
        }

    RETURN_TYPES = ("CONDITIONING", "CONDITIONING", "STRING", "STRING")
    RETURN_NAMES = ("Clip_Cond_Positive", "Clip_Cond_Negative", "Positive_Text", "Negative_Text")
    OUTPUT_TOOLTIPS = (
        "Connect this conditioning output to nodes that accept positive conditioning.",
        "Connect this conditioning output to nodes that accept negative conditioning.",
        "Connect this output to another nodes text (STRING) input.",
        "Connect this output to another nodes text (STRING) input."
    )
    FUNCTION = "encode_text"
    CATEGORY = "Custom EXO Nodes"

    def encode_text(self, Clip_Input, Positive_Text, Negative_Text):
        """
        Encodes positive and negative text prompts into CLIP embeddings.
        
        Args:
            Clip_Input: The CLIP model used for encoding
            Positive_Text (str): The positive prompt text
            Negative_Text (str): The negative prompt text
            
        Returns:
            tuple: (positive_conditioning, negative_conditioning, positive_text, negative_text)
        """
        # Ensure proper UTF-8 encoding to handle special characters
        def ensure_utf8(text):
            if isinstance(text, bytes):
                return text.decode('utf-8')
            elif isinstance(text, str):
                return text.encode('utf-8').decode('utf-8')
            return text

        Positive_Text = ensure_utf8(Positive_Text)
        Negative_Text = ensure_utf8(Negative_Text)

        # Convert text to tokens for CLIP processing
        positive_tokens = Clip_Input.tokenize(Positive_Text)
        negative_tokens = Clip_Input.tokenize(Negative_Text)

        # Generate embeddings from tokens
        positive_output = Clip_Input.encode_from_tokens(positive_tokens, return_pooled=True, return_dict=True)
        negative_output = Clip_Input.encode_from_tokens(negative_tokens, return_pooled=True, return_dict=True)

        # Extract the primary conditioning tensors
        cond_positive = positive_output.pop("cond")
        cond_negative = negative_output.pop("cond")

        return (
            [[cond_positive, positive_output]], 
            [[cond_negative, negative_output]], 
            Positive_Text, 
            Negative_Text
        )

# Register the node with ComfyUI
NODE_CLASS_MAPPINGS = {
    "ComfyUI_EXO_Clip_Text_Encode": ComfyUI_EXO_Clip_Text_Encode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ComfyUI_EXO_Clip_Text_Encode": "ComfyUI EXO Clip Text Encode 👑",
}
