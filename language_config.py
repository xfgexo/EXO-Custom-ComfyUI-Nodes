# 
# language_config.py
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
language_config.py
-----------------------------
The Language Configuration module is used with the EXO Translate Text Node for managing language settings and preferences. This module contains the configuration of language-specific parameters, enabling integration and processing.
"""

import yaml
import os
import locale

# Custom directory for language files
LANGUAGE_DIR = os.path.join(os.path.dirname(__file__), "languages")

# Detect the system's default language
default_locale = locale.getdefaultlocale()[0]
if default_locale:
    default_language = default_locale.split('_')[0]
else:
    default_language = "en"

# Load language settings
def load_language_settings(language_code):
    language_file = f"{language_code}.yaml"
    with open(os.path.join(LANGUAGE_DIR, language_file), "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

language_settings = load_language_settings(default_language)

