# 
# _init_.py
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
__init__.py
-----------------------------
The ComfyUI EXO Nodes __init__.py Initialization node is a component that orchestrates the loading and integration of custom nodes within the ComfyUI. This module ensures that all node mappings are correctly initialized.

Features:
- Node Mapping Initialization: Automatically loads and updates node class and display name mappings..
- System Path Management: Appends the current directory to the system path.
- Web Directory: Configures the web directory path for loading associated JavaScript files.
"""

import os
import platform
import sys

# Print ASCII art to console before loading node mappings
def display_ascii_art():
    ascii_art = """
\033[33m          )      )        )     )  (           (     
\033[33m       ( /(   ( /(     ( /(  ( /(  )\ )        )\ )  
\033[33m (     )\())  )\())    )\()) )\())(()/(   (   (()/(  
\033[33m )\   ((_)\  ((_)\    ((_)\ ((_)\  /(_))  )\   /(_)) 
\033[33m((\033[35m_\033[33m)  __((_)   ((_)   \033[35m _\033[33m((\033[35m_\033[33m)  ((_)(_))_  ((_) (_))   
\033[35m| __|\033[31m \ \/ /  / _ \   \033[35m| \| |\033[31m / _ \ |   \ | __|/ __|  
\033[35m| _|\033[31m   >  <  | (_) |  \033[35m| .` |\033[31m| (_) || |) || _| \__ \  
\033[35m|___|\033[31m /_/\_\  \___/   \033[35m|_|\_|\033[31m \___/ |___/ |___||___/    \033[0m                                                           

\033[31m...Loading EXO Node's\033[0m
""" 
    print(ascii_art)
display_ascii_art()

# Append the directory of the current file to the system path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import nodes
from .ComfyUI_EXO_Notes import NODE_CLASS_MAPPINGS as NotesMappings, NODE_DISPLAY_NAME_MAPPINGS as NotesDisplayNames
from .ComfyUI_EXO_SaveText import NODE_CLASS_MAPPINGS as SaveTextMappings, NODE_DISPLAY_NAME_MAPPINGS as SaveTextDisplayNames
from .ComfyUI_EXO_FluxSampler import NODE_CLASS_MAPPINGS as FluxSamplerMappings, NODE_DISPLAY_NAME_MAPPINGS as FluxSamplerDisplayNames
from .ComfyUI_EXO_DisplayText import NODE_CLASS_MAPPINGS as DisplayTextMappings, NODE_DISPLAY_NAME_MAPPINGS as DisplayTextDisplayNames
from .ComfyUI_EXO_NumericValue import NODE_CLASS_MAPPINGS as NumericValueMappings, NODE_DISPLAY_NAME_MAPPINGS as NumericValueDisplayNames
from .ComfyUI_EXO_ImageRescale import NODE_CLASS_MAPPINGS as ImageRescaleMappings, NODE_DISPLAY_NAME_MAPPINGS as ImageRescaleDisplayNames
from .ComfyUI_EXO_TranslateText import NODE_CLASS_MAPPINGS as TranslateTextMappings, NODE_DISPLAY_NAME_MAPPINGS as TranslateTextDisplayNames
from .ComfyUI_EXO_FluxSampler_Mini import NODE_CLASS_MAPPINGS as FluxSamplerMiniMappings, NODE_DISPLAY_NAME_MAPPINGS as FluxSamplerMiniDisplayNames
from .ComfyUI_EXO_Clip_Text_Encode import NODE_CLASS_MAPPINGS as ClipTextMappings, NODE_DISPLAY_NAME_MAPPINGS as ClipTextDisplayNames
from .ComfyUI_EXO_LatentImageSize import NODE_CLASS_MAPPINGS as LatentImageSizeMappings, NODE_DISPLAY_NAME_MAPPINGS as LatentImageSizeDisplayNames
from .ComfyUI_EXO_LatentImageSizeX import NODE_CLASS_MAPPINGS as LatentImageSizeXMappings, NODE_DISPLAY_NAME_MAPPINGS as LatentImageSizeXDisplayNames
from .ComfyUI_EXO_PromptBuilderDeluxe import NODE_CLASS_MAPPINGS as DeluxeMappings, NODE_DISPLAY_NAME_MAPPINGS as DeluxeDisplayNames

# Initialize NODE_CLASS_MAPPINGS and NODE_DISPLAY_NAME_MAPPINGS
NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

# Update mappings with existing nodes
NODE_CLASS_MAPPINGS.update(NotesMappings)
NODE_CLASS_MAPPINGS.update(SaveTextMappings)
NODE_CLASS_MAPPINGS.update(FluxSamplerMappings)
NODE_CLASS_MAPPINGS.update(DisplayTextMappings)
NODE_CLASS_MAPPINGS.update(NumericValueMappings)
NODE_CLASS_MAPPINGS.update(ImageRescaleMappings)
NODE_CLASS_MAPPINGS.update(TranslateTextMappings)
NODE_CLASS_MAPPINGS.update(FluxSamplerMiniMappings)
NODE_CLASS_MAPPINGS.update(ClipTextMappings)
NODE_CLASS_MAPPINGS.update(LatentImageSizeMappings)
NODE_CLASS_MAPPINGS.update(LatentImageSizeXMappings)
NODE_CLASS_MAPPINGS.update(DeluxeMappings)

# Update display names for all nodes
NODE_DISPLAY_NAME_MAPPINGS.update(NotesDisplayNames)
NODE_DISPLAY_NAME_MAPPINGS.update(SaveTextDisplayNames)
NODE_DISPLAY_NAME_MAPPINGS.update(FluxSamplerDisplayNames)
NODE_DISPLAY_NAME_MAPPINGS.update(DisplayTextDisplayNames)
NODE_DISPLAY_NAME_MAPPINGS.update(NumericValueDisplayNames)
NODE_DISPLAY_NAME_MAPPINGS.update(ImageRescaleDisplayNames)
NODE_DISPLAY_NAME_MAPPINGS.update(TranslateTextDisplayNames)
NODE_DISPLAY_NAME_MAPPINGS.update(FluxSamplerMiniDisplayNames)
NODE_DISPLAY_NAME_MAPPINGS.update(ClipTextDisplayNames)
NODE_DISPLAY_NAME_MAPPINGS.update(LatentImageSizeDisplayNames)
NODE_DISPLAY_NAME_MAPPINGS.update(LatentImageSizeXDisplayNames)
NODE_DISPLAY_NAME_MAPPINGS.update(DeluxeDisplayNames)

# Set web directory for loading JavaScript
WEB_DIRECTORY = "./web"
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]

