# 
# ComfyUI_EXO_Notes.py
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
EXO Notes Node 👑
-----------------------------
A simple text entry node that allows adding multiline notes directly within the nodes UI.

Features:
- Multiline Support: Provides a multiline text area for detailed note-taking.

Input Parameters:
- Notes_Text: A multiline text input for entering notes, with a default message "Enter your notes here..."

Output:
- Display Notes: Displays the entered notes within the workflow for easy reference.
"""


class ComfyUI_EXO_Notes:
    
    def __init__(self):
        self.type = "output"

    @classmethod
    def INPUT_TYPES(s):
        """
        Defines the input interface for the notes node.
        Creates a multiline text area for entering notes.
        """
        return {
            "required": {
                "Notes_Text": ("STRING", {
                    "multiline": True,
                    "default": "Enter your notes here...",
                    "tooltip": "Enter any notes or documentation for your workflow here."
                }),
            }
        }
    
    RETURN_TYPES = ()
    FUNCTION = "display_notes"
    CATEGORY = "Custom EXO Nodes"
    OUTPUT_NODE = True

    def display_notes(self, Notes_Text):
        """
        Displays the notes text in the ComfyUI interface.
        Returns a UI update dictionary containing the text to display.
        """
        return {
            "ui": {
                "text": Notes_Text
            },
        }

# Register the node with ComfyUI
NODE_CLASS_MAPPINGS = {
    "ComfyUI_EXO_Notes": ComfyUI_EXO_Notes,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ComfyUI_EXO_Notes": "ComfyUI EXO Notes 👑",
}

