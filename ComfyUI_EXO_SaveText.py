# 
# ComfyUI_EXO_SaveText.py
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
EXO Save Text Node 👑
-----------------------------
The ComfyUI EXO Save Text Node is a robust component designed for efficiently saving prompt text to files within ComfyUI workflows. This node supports both positive and negative prompts and offers versatile file operations, including append and overwrite functionalities.

Features:
- File Operations: Choose from Append, Overwrite, Ignore, or Erase.
- Timestamped Entries: Automatically includes the current date and time with each saved entry.
- UTF-8 Encoding: Guarantees proper text encoding, supporting diverse characters and languages.

Inputs:
- Positive_Text: The positive prompt text to be saved.
- Negative_Text: The negative prompt text to be saved.
- File_Action: The file operation to perform (Append, Overwrite, Ignore, Erase).
- File_Name: The name of the file to save the prompts in, including the .txt extension.
- Output_Folder: The folder where the prompt file will be saved.

Outputs:
- This node is an output node, performing file operations without producing a data output.

"""

import os
import folder_paths
import json
from server import PromptServer
import glob
from aiohttp import web
from datetime import datetime

def get_allowed_dirs():
    """Set up and return the allowed directories for file operations."""
    dirs = {
        "output": folder_paths.get_output_directory(),
        "Prompt_Output": os.path.join(folder_paths.get_output_directory(), "Prompt_Output")
    }
    if not os.path.exists(dirs["Prompt_Output"]):
        os.makedirs(dirs["Prompt_Output"])
    return dirs

def get_valid_dirs():
    """Get the list of valid directory names."""
    return get_allowed_dirs().keys()

def get_dir_from_name(name):
    """Convert a directory name to its full path."""
    dirs = get_allowed_dirs()
    if name not in dirs:
        raise KeyError(name + " dir not found")
    return dirs[name]

def is_child_dir(parent_path, child_path):
    """Verify if a path is a child of another path for security."""
    parent_path = os.path.abspath(parent_path)
    child_path = os.path.abspath(child_path)
    return os.path.commonpath([parent_path]) == os.path.commonpath([parent_path, child_path])

def get_real_path(dir):
    """Convert a glob pattern to a real directory path."""
    dir = dir.replace("/**/", "/")
    dir = os.path.abspath(dir)
    dir = os.path.split(dir)[0]
    return dir

@PromptServer.instance.routes.get("/comfyui_exo/save-text/{name}")
async def get_files(request):
    """API endpoint to get list of files in a directory."""
    name = request.match_info["name"]
    dir = get_dir_from_name(name)
    recursive = "/**/" in dir
    pre = get_real_path(dir)

    files = list(map(lambda t: os.path.relpath(t, pre),
                     glob.glob(dir, recursive=recursive)))
    if len(files) == 0:
        files = ["[none]"]
    return web.json_response(files)

def get_file(root_dir, file):
    """Get the full path for a file while ensuring it's in an allowed directory."""
    root_dir = get_dir_from_name(root_dir)
    if not os.path.exists(root_dir):
        os.makedirs(root_dir)
    full_path = os.path.join(root_dir, file)
    if not is_child_dir(root_dir, full_path):
        raise ReferenceError(f"File {file} is not within the allowed directory: {root_dir}")
    return full_path

class TextFileNodeExo:
    """Base class for text file operations."""
    RETURN_TYPES = ()
    CATEGORY = "Custom EXO Nodes"

    @classmethod
    def VALIDATE_INPUTS(cls, **kwargs):
        """Validate file paths before operations."""
        root_dir = kwargs.get("Output_Folder")
        file = kwargs.get("File_Name")
        if file == "[none]" or not file or not file.strip():
            return True
        get_file(root_dir, file)
        return True

class ComfyUI_EXO_SaveText(TextFileNodeExo):
    """
    A ComfyUI node that saves prompt text to files.
    Supports multiple file operations and includes timestamps.
    """
    OUTPUT_NODE = True

    @classmethod
    def IS_CHANGED(self, **kwargs):
        return float("nan")

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "Positive_Text": ("STRING", {
                    "forceInput": True, 
                    "multiline": False, 
                    "placeholder": "Connect Positive Prompt",
                    "tooltip": "Connect this input to another nodes text (STRING) output."
                }),
                "Negative_Text": ("STRING", {
                    "forceInput": True, 
                    "multiline": False, 
                    "placeholder": "Connect Negative Prompt",
                    "tooltip": "Connect this input to another nodes text (STRING) output."
                }),
                "File_Action": (["Ignore", "Append", "Overwrite", "Erase"], {
                    "tooltip": "Select how to handle the file: Append (add to end), Overwrite (replace content), Ignore (skip saving), or Erase (clear file)."
                }),
                "File_Name": ("STRING", {
                    "default": "Prompt_File.txt", 
                    "placeholder": "Enter file name",
                    "tooltip": "Name of the file to save the prompts in. Include .txt extension."
                }),
                "Output_Folder": (list(get_valid_dirs()), {
                    "default": "Prompt_Output",
                    "tooltip": "Select the folder where the prompt file will be saved."
                }),
            },
        }

    FUNCTION = "write_text"

    def write_text(self, Output_Folder=None, File_Name=None, File_Action=None, Positive_Text=None, Negative_Text=None):
        """
        Write text to file based on selected action.
        
        Args:
            Output_Folder (str): Directory to save the file
            File_Name (str): Name of the file to save
            File_Action (str): The action to perform (Append/Overwrite/Ignore/Erase)
            Positive_Text (str): The positive prompt text
            Negative_Text (str): The negative prompt text
        """
        placeholder_text = "***No Prompt Text Available***"
        positive_prompt = "".join(Positive_Text) if Positive_Text.strip() else placeholder_text
        negative_prompt = "".join(Negative_Text) if Negative_Text.strip() else placeholder_text

        # Ensure proper UTF-8 encoding for all text
        def ensure_utf8(text):
            if isinstance(text, bytes):
                return text.decode('utf-8')
            elif isinstance(text, str):
                return text.encode('utf-8').decode('utf-8')
            return text

        positive_prompt = ensure_utf8(positive_prompt)
        negative_prompt = ensure_utf8(negative_prompt)

        # Handle Ignore action
        if File_Action == "Ignore":
            print("\033[93mText file saving is disabled. Skipping write operation.\033[0m")
            return ()

        # Set up file path
        output_folder = Output_Folder if isinstance(Output_Folder, str) else Output_Folder[0]
        file_name = File_Name if isinstance(File_Name, str) else File_Name[0]
        file_path = get_file(output_folder, file_name)

        # Handle Erase action
        if File_Action == "Erase":
            if os.path.exists(file_path):
                open(file_path, "w").close()
                print(f"\033[92mFile '{file_name}' erased successfully.\033[0m")
            else:
                print(f"\033[91mFile '{file_name}' does not exist. Nothing to erase.\033[0m")
            return ()

        # Format current timestamp
        current_datetime = datetime.now()
        formatted_date = current_datetime.strftime("%m-%d-%Y")
        formatted_time = current_datetime.strftime("%I:%M %p")

        # Prepare the text to write
        date_time_text = f"Date: {formatted_date} - Time: {formatted_time}\n"
        positive_text = f"Positive Prompt: {positive_prompt}\n\n"
        negative_text = f"Negative Prompt: {negative_prompt}\n\n\n"
        full_text = f"{date_time_text}{positive_text}{negative_text}"

        # Validate output directory
        if output_folder not in get_valid_dirs():
            raise KeyError(f"'{output_folder}' is not a valid directory. Choose from: {list(get_valid_dirs())}")

        # Write the file based on selected action
        file_action = File_Action if isinstance(File_Action, str) else File_Action[0]
        with open(file_path, "a+" if file_action == "Append" else "w", encoding='utf-8') as f:
            f.write(full_text)

        # Print appropriate success message
        if file_action == "Append":
            print(f"\033[94mFile '{file_name}' appended successfully.\033[0m")
        elif file_action == "Overwrite":
            print(f"\033[95mFile '{file_name}' overwritten successfully.\033[0m")

        return ()

# Register the node with ComfyUI
NODE_CLASS_MAPPINGS = {
    "ComfyUI_EXO_SaveText": ComfyUI_EXO_SaveText,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ComfyUI_EXO_SaveText": "ComfyUI EXO Save Text 👑",
}
