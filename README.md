<h1  align="left">EXO-Custom-ComfyUI-Nodes</h1>

This repository contains all the custom nodes I originally made for myself for ComfyUI. However, I have decided to make them available to everyone.

<div  align="center">
<img  height="40"  src="https://github.com/xfgexo/EXO-Custom-ComfyUI-Nodes/blob/EXO_ComfyUI/images/git_divider2.png"  />
</div>

<h3  align="center">ComfyUI EXO Prompt Builder Deluxe Node</h3>
<h4  align="left">EXO Prompt Builder Deluxe 👑<br>-----------------------------</h4>Designed for dynamic prompt creation and template management within ComfyUI. This advanced node goes beyond what standard text prompts and styler nodes can do by offering a modular system that allows users to construct complex text prompts. It utilizes over 90 JSON file templates, each containing 50 to 80 entries and each entry having its own unique keywords, which in turn provides a wide selection of options for a truly dynamic and creative process. The node supports both template and manual and combined inputs.<br><br>A standout feature of the Prompt Builder Deluxe Node is its comprehensive suite of options for character creation. It offers users a way to design every aspect of a character, everything from environmental settings to intricate details such as facial features, hair design, body and skin attributes, accessories, art styles and more. Users can select from a broad range of presets or customize each element to their own liking. Whether crafting a character's physical appearance, outfit, or choosing a quick preset, this node has it all.<br><br>Features:<br>- Dynamic Prompt Building: Combines prompt templates from multiple categories.<br>- Extensive Template Library: Utilizes 90 JSON file templates.<br>- Manual Input Support: Allows for manual input of text prompts.<br>- Template Management: Utilizes a modular system for managing and organizing prompt templates.<br>- Configuration File: Easily edit a config file to modify sort order and rename labels and entries.<br>- Section Toggles: Ability to Enable/Disable category sections.<br>- Category Selections: Easily selectable drop-down lists of categories.<br>- Console Logging: Offers an option to log combined prompts to the console.<br><br>Inputs:<br>- Positive_Prompt_Text: Manually entered positive prompt text.<br>- Negative_Prompt_Text: Manually entered negative prompt text.<br>- Log_Prompt_to_Console: Input toggle to enable or disable console logging of the combined prompts.<br>- Section Toggles: Boolean inputs for enabling or disabling specific sections of templates.<br>- Category Selections: Dropdowns for selecting specific templates from each category.<br><br>Outputs:<br>- Positive_Prompt_Text: The combined positive prompt text.<br>- Negative_Prompt_Text: The combined negative prompt text.<br><br>

<div  align="center">

<img  height="2816"  src="https://github.com/xfgexo/EXO-Custom-ComfyUI-Nodes/blob/EXO_ComfyUI/images/git_exo_pbd_ss.png"  />
</div>
<br>
<div  align="center">
<img  height="40"  src="https://github.com/xfgexo/EXO-Custom-ComfyUI-Nodes/blob/EXO_ComfyUI/images/git_divider2.png"  />
</div>

<h3  align="center">ComfyUI EXO Translate Text Node</h3>
<h4  align="left">EXO Translate Text 👑<br>-----------------------------</h4>A powerful node for translating text between multiple languages within ComfyUI workflows.<br><br>Modes:<br>- Ignore: Pass-through functionality without translation.<br>- Translation: Utilizes MarianMT models from the Helsinki-NLP project for translation.<br><br>Features:<br>- Multilingual Translation from English to Chinese, French, German, Japanese, Spanish. <br>- Multilingual Translation from Chinese, French, German, Japanese, Spanish to English.<br>- Model Caching: Auto Downloads and caches models on first use.<br>- Language Detection: Detects the source language to avoid unnecessary translations.<br>- UTF-8 Encoding: Ensures proper text encoding, supporting diverse characters and languages.<br><br>Inputs:<br>- Positive_Text: The positive prompt text to be translated.<br>- Negative_Text: The negative prompt text to be translated.<br>- Translation_Model: Selects the translation language direction.<br><br>Outputs:<br>- Trans_Positive_Text: The translated positive text.<br>- Trans_Negative_Text: The translated negative text.<br>

<div  align="center">
<img  height="210"  src="https://github.com/xfgexo/EXO-Custom-ComfyUI-Nodes/blob/EXO_ComfyUI/images/git_exo_translatetext_ss.png"  />
</div>
<br>
<div  align="center">
<img  height="40"  src="https://github.com/xfgexo/EXO-Custom-ComfyUI-Nodes/blob/EXO_ComfyUI/images/git_divider2.png"  />
</div>

<h3  align="center">ComfyUI EXO Clip Text Encode Node</h3>
<h4  align="left">EXO Clip Text Encode 👑<br>-----------------------------</h4>Features:<br>- Dual Prompt Handling: This node processes both positive and negative text prompts.<br>- Encoding: Utilizes CLIP models to convert text inputs into conditioning tensors.<br>- UTF-8 Compatibility: Ensures that text inputs are properly encoded in UTF-8.<br><br>Inputs:<br>- Clip_Input: Connect this to the output of a loaded CLIP model.<br>- Positive_Text: A multiline string input for positive prompts.<br>- Negative_Text: A multiline string input for negative prompts.<br><br>Outputs:<br>- Clip_Cond_Positive: The positive conditioning tensor.<br>- Clip_Cond_Negative: The negative conditioning tensor.<br>- Positive_Text: The original positive text prompt, available for downstream use.<br>- Negative_Text: The original negative text prompt, available for downstream use.<br>

<div  align="center">
<img  height="210"  src="https://github.com/xfgexo/EXO-Custom-ComfyUI-Nodes/blob/EXO_ComfyUI/images/git_exo_textencode_ss.png"  />
</div>
<br>
<div  align="center">
<img  height="40"  src="https://github.com/xfgexo/EXO-Custom-ComfyUI-Nodes/blob/EXO_ComfyUI/images/git_divider2.png"  />
</div>

<h3  align="center">ComfyUI EXO Display Text Node</h3>
<h4  align="left">EXO Display Text 👑<br>-----------------------------</h4>The ComfyUI EXO Display Text node is a custom node designed to display and pass through text content within the ComfyUI nodes UI. It provides a visual representation of both positive and negative prompts while allowing the text to continue through the workflow downstream.<br><br>Features:<br>- Text Display: Displays both positive and negative text prompts in the UI.<br>- Pass-Through Capability: Maintains the ability to connect to downstream nodes.<br>- UTF-8 Compatibility: Ensures that text inputs are properly encoded in UTF-8.<br><br>Inputs:<br>- Positive_Text: A multiline string input for positive prompts.<br>- Negative_Text: A multiline string input for negative prompts.<br><br>Outputs<br>- Positive_Text: The original positive text prompt, passed through for further processing.<br>- Negative_Text: The original negative text prompt, passed through for further processing.<br>

 <div  align="center">
<img  height="484"  src="https://github.com/xfgexo/EXO-Custom-ComfyUI-Nodes/blob/EXO_ComfyUI/images/git_exo_displaytext_ss.png"  />
</div>
<br>
<div  align="center">
<img  height="40"  src="https://github.com/xfgexo/EXO-Custom-ComfyUI-Nodes/blob/EXO_ComfyUI/images/git_divider2.png"  />
</div>

<h3  align="center">ComfyUI EXO Save Text Node</h3>
<h4  align="left">EXO Save Text 👑<br>-----------------------------</h4>The ComfyUI EXO Save Text Node is a robust component designed for efficiently saving prompt text to files within ComfyUI workflows. This node supports both positive and negative prompts and offers versatile file operations, including append and overwrite functionalities.<br><br>Features:<br>- File Operations: Choose from Append, Overwrite, Ignore, or Erase.<br>- Timestamped Entries: Automatically includes the current date and time with each saved entry.<br>- UTF-8 Encoding: Guarantees proper text encoding, supporting diverse characters and languages.<br><br>Inputs:<br>- Positive_Text: The positive prompt text to be saved.<br>- Negative_Text: The negative prompt text to be saved.<br>- File_Action: The file operation to perform (Append, Overwrite, Ignore, Erase).<br>- File_Name: The name of the file to save the prompts in, including the .txt extension.<br>- Output_Folder: The folder where the prompt file will be saved.<br><br>Outputs:<br>- This node is an output node, performing file write and save operations.<br>

 <div  align="center">
<img  height="243"  src="https://github.com/xfgexo/EXO-Custom-ComfyUI-Nodes/blob/EXO_ComfyUI/images/git_exo_savetext_ss.png"  />
</div>
<br>
<div  align="center">
<img  height="40"  src="https://github.com/xfgexo/EXO-Custom-ComfyUI-Nodes/blob/EXO_ComfyUI/images/git_divider2.png"  />
</div>

<h3  align="center">ComfyUI EXO Numeric Value Node</h3>
<h4  align="left">EXO Numeric Value 👑<br>-----------------------------</h4>The ComfyUI EXO Numeric Value node is a simple yet essential node for numeric entry within the ComfyUI workflow. It allows users to input a numeric value, outputting it as a float for use in subsequent nodes.<br><br>Features:<br>- Numeric Input: Provides a straightforward interface for entering numeric values, supporting float precision.<br>- Seamless Integration: Designed to connect easily with nodes that require numeric inputs.<br><br>Inputs:<br>- Numeric_Value: A float input field for entering the desired numeric value.<br><br>Outputs:<br>- Numeric_Value: The entered numeric value, output as a float for use in other nodes.<br>

<div  align="center">
<img  height="135"  src="https://github.com/xfgexo/EXO-Custom-ComfyUI-Nodes/blob/EXO_ComfyUI/images/git_exo_numeric_ss.png"  />
</div>
<br>
<div  align="center">
<img  height="40"  src="https://github.com/xfgexo/EXO-Custom-ComfyUI-Nodes/blob/EXO_ComfyUI/images/git_divider2.png"  />
</div>

<h3  align="center">ComfyUI EXO Latent Image Size Node<br>ComfyUI EXO Latent Image Size X Node</h3>
<h4  align="left">EXO Latent Image Size 👑<br>-----------------------------</h4>The ComfyUI EXO Latent Image Size node is a customizable node within ComfyUI. Designed to generate latent images based on user-selected dimensions. It facilitates the creation of latent image noise for further processing in workflows.<br><br>Features:<br>- Dimension Selection: Select from predefined dimensions.<br>- Batch Processing: Supports generating multiple images in a single batch.<br>- Configurable Defaults: Easily edit an external JSON configuration file, allowing for easy customization.<br>- Format: The format is "width x height (aspect ratio).<br><br>Inputs:<br>- Dimensions: A dropdown selection for choosing the desired dimensions of the latent image. <br>- Batch_Size: An integer input specifying the number of images to generate in a single batch.<br><br>Outputs:<br>- Latent: The generated latent image noise at the specified dimensions.<br><br><h4  align="left">EXO Latent Image Size X 👑<br>-----------------------------</h4>The ComfyUI EXO Latent Image Size X node is an enhanced version of the latent image size node within the ComfyUI framework. It allows for the generation of latent images with additional outputs for width and height, providing greater flexibility in workflow integration.<br><br>Features<br>- Dimension Selection: Select from predefined dimensions.<br>- Batch Processing: Supports generating multiple images in a single batch.<br>- Configurable Defaults: Easily edit an external JSON configuration file, allowing for easy customization.<br>- Format: The format is "width x height (aspect ratio).<br>- Additional Outputs: Provides separate outputs for the width and height of the selected dimensions.<br><br>Inputs:<br>- Dimensions: A dropdown selection for choosing the desired dimensions of the latent image.<br>- Batch_Size: An integer input specifying the number of images to generate in a single batch.<br><br>Outputs:<br>- Latent: The generated latent image noise at the specified dimensions.<br>- Width: The width of the selected dimensions in pixels.<br>- Height: The height of the selected dimensions in pixels.<br>

<div  align="center">
<img  height="759"  src="https://github.com/xfgexo/EXO-Custom-ComfyUI-Nodes/blob/EXO_ComfyUI/images/git_exo_latent_ss.png"  />
</div>
<br>
<div  align="center">
<img  height="40"  src="https://github.com/xfgexo/EXO-Custom-ComfyUI-Nodes/blob/EXO_ComfyUI/images/git_divider2.png"  />
</div>

<h3  align="center">ComfyUI EXO Image Rescale Node</h3>
<h4  align="left">EXO Image Rescale 👑<br>-----------------------------</h4>A versatile image rescaling node for ComfyUI that provides multiple scaling modes:<br><br>Modes:<br>- Ignore: Passes the image through without any modifications<br>- Resize: Resizes the image to specific width and height dimensions<br>- Upscale: Enlarges the image by a specified scale factor<br>- Downscale: Reduces the image by a specified scale factor<br><br>Features:<br>- Multiple resampling methods (lanczos, nearest, bilinear, bicubic)<br>- Supersampling anti-aliasing option for higher quality results<br>- Maintains proper tensor format for ComfyUI compatibility<br>- Configurable scale factors via external JSON configuration<br><br>Input Parameters:<br>- Image: Input image tensor<br>- Mode: Scaling mode selection<br>- Scale_Factor: Multiplier for upscale/downscale operations<br>- Resize_Width: Target width for resize mode<br>- Resize_Height: Target height for resize mode<br>- Resampling: Algorithm used for resizing<br>- Supersample: Anti-aliasing method selection<br>- Force_Resize: Option to force exact dimensions<br><br>Output:<br>- Processed image tensor in the correct format for ComfyUI (B,C,H,W)<br>

<div  align="center">
<img  height="307"  src="https://github.com/xfgexo/EXO-Custom-ComfyUI-Nodes/blob/EXO_ComfyUI/images/git_exo_rescale_ss.png"  />
</div>
<br>
<div  align="center">
<img  height="40"  src="https://github.com/xfgexo/EXO-Custom-ComfyUI-Nodes/blob/EXO_ComfyUI/images/git_divider2.png"  />
</div>

<h3  align="center">ComfyUI EXO FluxSampler Node<br>ComfyUI EXO FluxSampler Mini Node</h3>
<h4  align="left">ComfyUI EXO FluxSampler 👑<br>-----------------------------</h4>The ComfyUI EXO FluxSampler node is an advanced sampling node designed for ComfyUI. It provides flexible and customizable sampling capabilities, allowing for precise control over model sampling.<br><br>Features:<br>- Customizable Sampling: Including noise seed, increment value, sampler name, scheduler, and more.<br>- Model Sampling: Utilizes a custom ModelSamplingFlux logic.<br>- Noise Generation: Includes a built-in noise generator.<br>- Guidance Integration: Supports conditioning guidance.<br><br>Inputs:<br>- Model: The model to be used for sampling.<br>- Conditioning: The conditioning tensor for guiding the sampling process.<br>- Width and Height: Dimensions for the output image.<br>- Noise_Seed: Seed for noise generation, ensuring reproducibility.<br>- Increment_Value: Increment value for sampling adjustments.<br>- Sampler_Name: Chooses the sampler algorithm.<br>- Scheduler: Selects the scheduling method for sigma generation.<br>- Steps: Number of steps for the sampling process.<br>- Denoise: Denoising factor for adjusting the sampling intensity.<br>- Max_Shift and Base_Shift: Parameters for controlling the sampling shift.<br>- Guidance: Guidance factor for conditioning adjustments.<br>- Negative_Conditioning (optional): Additional conditioning for negative guidance.<br><br>Outputs:<br>- Model_Out: The processed model with applied sampling.<br>- Noise: The generated noise object.<br>- Sampler: The sampler object used for processing.<br>- Sigmas: The computed sigmas for the sampling process.<br>- Seed: The seed dictionary for noise generation.<br>- Latent: The generated latent image tensor.<br>- Guider: The guidance object for conditioning.<br>- Conditioning_Out: The adjusted conditioning tensor with applied guidance.<br>

<h4  align="left">EXO FluxSampler Mini 👑<br>-----------------------------</h4>The ComfyUI EXO FluxSampler Mini node is an sampling node designed for ComfyUI. It provides flexible sampling capabilities, allowing for control over model sampling.<br><br>Features:<br>- Model Sampling: Utilizes a custom ModelSamplingFlux logic.<br><br>Inputs:<br>- Model: The model to be used for sampling.<br>- Width and Height: Dimensions for the output image.<br>- Max_Shift: Parameters for controlling the sampling shift.<br>- Base_Shift: Parameters for controlling the sampling shift.<br><br>Outputs:<br>- Model_Out: The processed model with applied sampling.<br>

<div  align="center">
<img  height="848"  src="https://github.com/xfgexo/EXO-Custom-ComfyUI-Nodes/blob/EXO_ComfyUI/images/git_exo_flux_samp_ss.png"  />
</div>
<br>
<div  align="center">
<img  height="40"  src="https://github.com/xfgexo/EXO-Custom-ComfyUI-Nodes/blob/EXO_ComfyUI/images/git_divider2.png"  />
</div>

<h3  align="center">ComfyUI EXO Notes Node</h3>
<h4  align="left">EXO Notes 👑<br>-----------------------------</h4>A simple text entry node that allows adding multiline notes directly within the nodes UI.<br><br>Features:<br>- Multiline Support: Provides a multiline text area for detailed note-taking.<br><br>Input Parameters:<br>- A multiline text input for entering notes, with a default message "Enter your notes here..."<br><br>Output:<br>- Displays the entered notes within the workflow for easy reference.<br>

<div  align="center">
<img  height="848"  src="https://github.com/xfgexo/EXO-Custom-ComfyUI-Nodes/blob/EXO_ComfyUI/images/git_exo_notes_ss.png"  />
</div>
<br>
<div  align="center">
<img  height="40"  src="https://github.com/xfgexo/EXO-Custom-ComfyUI-Nodes/blob/EXO_ComfyUI/images/git_divider2.png"  />
</div>

<h3  align="left">Example Workflow's</h3>
I have included three workflow examples with my node package. The workflows support SDXL and FLUX.<br><br>The workflows:<br>You will find the workflows in the "workflows" folder of this package.<br>1. EXO Text to Image SDXL Workflow.json<br>2. EXO Image to Image SDXL Workflow.json<br>3. EXO Text to Image FLUX Workflow.json<br><br>Note: The workflows use nodes from the following node developers.<br>- ComfyUI core nodes<br>- ComfyUI EXO custom nodes<br><br>- ComfyUI-Detail-Daemon<br>https://github.com/Jonseed/ComfyUI-Detail-Daemon<br>- ComfyUI-Impact-Pack<br>https://github.com/ltdrdata/ComfyUI-Impact-Pack<br>- rgthree-comfy<br>https://github.com/rgthree/rgthree-comfy<br>
<br>
<div  align="center">
<img  height="780"  src="https://github.com/xfgexo/EXO-Custom-ComfyUI-Nodes/blob/EXO_ComfyUI/images/git_exo_tti_wf.jpg"  />
</div>
<br>
<div  align="center">
<img  height="40"  src="https://github.com/xfgexo/EXO-Custom-ComfyUI-Nodes/blob/EXO_ComfyUI/images/git_divider2.png"  />
</div>
<br>
<h3  align="left">Installation</h3>
To use the ComfyUI EXO custom nodes in your workflow, you now have two options:<br><br> A. **ComfyUI Manager**: You can now easily install the nodes directly from the ComfyUI Manager. Simply search for EXO Nodes in the search bar and then click Install.<br><br> B. **Manual Installation**: Follow these steps to manually install the EXO Node pack:<br><br> 1.) Navigate to the `custom_node` directory of your ComfyUI installation using Windows Explorer.<br> 2.) Then "Shift + Right click" inside the folder and choose either <br> `open in terminal`, `open in PowerShell`, or `get bash here`.<br> 3.) Then type in the following command to clone the repository:<br>

  ```git clone https://github.com/xfgexo/EXO-Custom-ComfyUI-Nodes.git```
<br>
Contributions to this project are welcome! If you encounter any issues or have suggestions for improvements, please feel free to [open an issue](https://github.com/xfgexo/EXO-Custom-ComfyUI-Nodes/issues)
<br>
<h3  align="left">License</h3>

_This custom ComfyUi node pack is free software: you can redistribute it and/or modify
<br>it under the terms of the GNU General Public License v3.0 as published
<br>by the Free Software Foundation.
<br> 
<br>This program is distributed in the hope that it will be useful,
<br>but WITHOUT ANY WARRANTY; without even the implied warranty of
<br>MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
<br>GNU General Public License for more details.
<br> 
<br>The GPL license ensures that any derivative work based on GPL-licensed code
<br>must also be distributed under the same GPL license terms. This means that if
<br>you modify GPL-licensed software and distribute your modified version, you must
<br>also provide the source code and allow others to modify and distribute it under
<br>the same GPL license.
<br> 
<br>A copy of the GNU General Public License is included within these project files._
<br>
<br>
.# Date: Dec.17.2024<br>
.# Author: Joe Porter / AKA: xfgexo<br>
.# URL Link: [EXO-Custom-ComfyUI-Nodes](https://github.com/xfgexo/EXO-Custom-ComfyUI-Nodes)