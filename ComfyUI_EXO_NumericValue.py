# 
# ComfyUI_EXO_NumericValue.py
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
EXO Numeric Value 👑
-----------------------------
The ComfyUI EXO Numeric Value node is a simple yet essential node for numeric entry within the ComfyUI workflow. It allows users to input a numeric value, outputting it as a float for use in subsequent nodes.

Features:
- Numeric Input: Provides a straightforward interface for entering numeric values, supporting float precision.
- Seamless Integration: Designed to connect easily with nodes that require numeric inputs.

Inputs:
- Numeric_Value: A float input field for entering the desired numeric value.

Outputs:
- Numeric_Value: The entered numeric value, output as a float for use in other nodes.
"""

class ComfyUI_EXO_NumericValue:
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "Numeric_Value": ("FLOAT", {"default": 0.05, "step": 0.01, "tooltip": "Enter a numeric value for output"}),
            }
        }

    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("Numeric_Value",)
    FUNCTION = "process_float"
    CATEGORY = "Custom EXO Nodes"
    
    # Output tooltip using the correct format
    OUTPUT_TOOLTIPS = ("Connect this output to a node that expects a Numeric value for its input.",)

    def process_float(self, Numeric_Value):
        """
        Returns the entered float value.
        
        Args:
            Numeric_Value (float): The numeric input provided by the user.
        
        Returns:
            float: The entered numeric value.
        """
        return (Numeric_Value,)

# Register node mappings
NODE_CLASS_MAPPINGS = {
    "ComfyUI_EXO_NumericValue": ComfyUI_EXO_NumericValue,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ComfyUI_EXO_NumericValue": "ComfyUI EXO Numeric Value 👑",
}
