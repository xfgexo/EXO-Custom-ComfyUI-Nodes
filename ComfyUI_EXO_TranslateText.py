# 
# ComfyUI_EXO_TranslateText.py
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
EXO Translate Text Node 👑
-----------------------------
A powerful node for translating text between multiple languages within ComfyUI workflows.

Modes:
- Ignore: Pass-through functionality without translation.
- Translation: Utilizes MarianMT models from the Helsinki-NLP project for translation.

Features:
- Multilingual Translation from English to Chinese, French, German, Japanese, Spanish. 
- Multilingual Translation from Chinese, French, German, Japanese, Spanish to English.
- Model Caching: Auto Downloads and caches models on first use.
- Language Detection: Detects the source language to avoid unnecessary translations.
- UTF-8 Encoding: Ensures proper text encoding, supporting diverse characters and languages.

Inputs:
- Positive_Text: The positive prompt text to be translated.
- Negative_Text: The negative prompt text to be translated.
- Translation_Model: Selects the translation language direction.

Outputs:
- Trans_Positive_Text: The translated positive text.
- Trans_Negative_Text: The translated negative text.
"""

from transformers import MarianMTModel, MarianTokenizer
import os
from tqdm import tqdm
import requests
from requests.exceptions import RequestException, ConnectionError, Timeout
from urllib3.exceptions import MaxRetryError
import comfy.utils
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException
import re

# Dictionary mapping user-friendly names to their corresponding model identifiers
# The 'None' values for "Ignore" and separator allow pass-through functionality
AVAILABLE_MODELS = {
    "Ignore": None,
    "English to Chinese (Simplified)": "Helsinki-NLP/opus-mt-en-zh",
    "English to French": "Helsinki-NLP/opus-mt-en-fr",
    "English to German": "Helsinki-NLP/opus-mt-en-de",
    "English to Japanese": "Helsinki-NLP/opus-mt-en-ja",
    "English to Spanish": "Helsinki-NLP/opus-mt-en-es",
    "-----": None,  # Visual separator in dropdown
    "Chinese (Simplified) to English": "Helsinki-NLP/opus-mt-zh-en",
    "French to English": "Helsinki-NLP/opus-mt-fr-en",
    "German to English": "Helsinki-NLP/opus-mt-de-en",
    "Japanese to English": "Helsinki-NLP/opus-mt-ja-en",
    "Spanish to English": "Helsinki-NLP/opus-mt-es-en",
}

# Store downloaded models locally in a subdirectory of the node's location
CUSTOM_MODEL_DIR = os.path.join(os.path.dirname(__file__), "translate_models")

class ComfyUI_EXO_TranslateText:
    """
    A ComfyUI node that provides text translation capabilities.
    Handles translation of both positive and negative prompts using Helsinki-NLP's MarianMT models.
    Models are downloaded and cached locally on first use.
    """
    
    def __init__(self):
        self.type = "function"
        self.model = None
        self.tokenizer = None

    @classmethod
    def INPUT_TYPES(s):
        """Define the input types and their configuration for the node."""
        return {
            "required": {
                "Positive_Text": ("STRING", {
                    "multiline": False, 
                    "forceInput": True, 
                    "tooltip": "Connect this input to another nodes text (STRING) output."
                }),
                "Negative_Text": ("STRING", {
                    "multiline": False, 
                    "forceInput": True, 
                    "tooltip": "Connect this input to another nodes text (STRING) output."
                }),
                "Translation_Model": (list(AVAILABLE_MODELS.keys()), {
                    "default": "Ignore", 
                    "tooltip": "Choose the language translation direction. Select 'Ignore' to pass through text without translation. Models will be downloaded on first use."
                }),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("Trans_Positive_Text", "Trans_Negative_Text")
    OUTPUT_TOOLTIPS = (
        "Connect this output to another nodes text (STRING) input.",
        "Connect this output to another nodes text (STRING) input."
    )
    FUNCTION = "translate_text"
    CATEGORY = "Custom EXO Nodes"

    def translate_text(self, Positive_Text, Negative_Text, Translation_Model):
        """
        Main processing function that handles text translation.
        
        Args:
            Positive_Text (str): The positive prompt text to translate
            Negative_Text (str): The negative prompt text to translate
            Translation_Model (str): The selected translation model name
            
        Returns:
            tuple: (translated_positive, translated_negative) - The translated texts
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

        # Handle special cases: "Ignore" and separator
        if Translation_Model in ["Ignore", "-----"]:
            return (Positive_Text, Negative_Text)

        # Get and configure the translation model
        model_name = AVAILABLE_MODELS[Translation_Model]
        os.environ["TRANSFORMERS_CACHE"] = CUSTOM_MODEL_DIR
        model_path = os.path.join(CUSTOM_MODEL_DIR, model_name.replace("/", "_"))

        # Download and setup model if not already available locally
        if not os.path.exists(model_path):
            print(f"Model '{model_name}' not found locally. Downloading the model...")
            try:
                # Show progress during download and setup
                total_steps = 3  # Model download, tokenizer download, saving
                pbar = comfy.utils.ProgressBar(total_steps)

                self.model = MarianMTModel.from_pretrained(model_name)
                pbar.update(1)
                self.tokenizer = MarianTokenizer.from_pretrained(model_name)
                pbar.update(1)

                # Cache the model locally
                self.model.save_pretrained(model_path)
                self.tokenizer.save_pretrained(model_path)
                pbar.update(1)
            except (RequestException, ConnectionError, Timeout, MaxRetryError) as e:
                error_message = f"Warning - model {model_name} failed to download.\nPlease check your internet connection."
                print(f"\033[91m{error_message}\033[0m")
                return (error_message, error_message)
            except Exception as e:
                error_message = f"Error downloading the model '{model_name}': {e}"
                print(f"\033[91m{error_message}\033[0m")
                return (error_message, error_message)
        else:
            # Load cached model
            self.model = MarianMTModel.from_pretrained(model_path)
            self.tokenizer = MarianTokenizer.from_pretrained(model_path)

        # Extract languages from model name for language detection
        source_language, target_language = Translation_Model.split(" to ")

        def translate_chunks(text):
            """
            Breaks text into chunks and translates each chunk separately.
            Attempts to detect the language to avoid unnecessary translations.
            """
            chunks = re.split(r'(?<=[.,])\s*', text)
            translated_chunks = []
            for chunk in chunks:
                try:
                    detected_language = detect(chunk)
                except LangDetectException:
                    detected_language = "unknown"

                # Only translate if the chunk isn't already in the target language
                if detected_language != target_language.lower():
                    inputs = self.tokenizer(chunk, return_tensors="pt", padding=True, truncation=True)
                    translated = self.model.generate(**inputs)
                    translated_text = self.tokenizer.decode(translated[0], skip_special_tokens=True)
                    translated_chunks.append(translated_text)
                else:
                    translated_chunks.append(chunk)
            return ' '.join(translated_chunks)

        # Process both texts
        translated_positive = translate_chunks(Positive_Text)
        translated_negative = translate_chunks(Negative_Text)

        return (translated_positive, translated_negative)

# Register the node with ComfyUI
NODE_CLASS_MAPPINGS = {
    "ComfyUI_EXO_TranslateText": ComfyUI_EXO_TranslateText,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ComfyUI_EXO_TranslateText": "ComfyUI EXO Translate Text 👑",
}
