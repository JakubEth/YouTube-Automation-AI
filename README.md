# Auto Video Creator

This project is designed to automatically generate videos using Stable Diffusion for image generation and Selenium for capturing CSS animations. The generated frames are compiled into a video using FFmpeg.

## Features

- **Image Generation**: Uses Stable Diffusion to generate frames based on a text prompt.
- **Video Compilation**: Compiles generated frames into a video using FFmpeg.
- **CSS Animation Capture**: Captures frames of a CSS animation using Selenium and Chrome in headless mode.

## Requirements

- Python 3.7+
- [Stable Diffusion](https://github.com/CompVis/stable-diffusion)
- [Selenium](https://www.selenium.dev/)
- [FFmpeg](https://ffmpeg.org/)
- [Torch](https://pytorch.org/)
- [PIL (Pillow)](https://python-pillow.org/)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/JakubEth/YouTube-Automation-AI
   cd YouTube-Automation-AI
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure FFmpeg is installed and available in your system's PATH.

4. Download and install the Chrome browser and ChromeDriver. Update the paths in `test_selenium.py` as needed.

## Usage

### Generate Video with Stable Diffusion

1. Run the `auto_video_creator.py` script:   ```bash
   python auto_video_creator.py   ```

2. The script will generate frames based on the specified prompt and compile them into a video.

### Capture CSS Animation

1. Run the `test_selenium.py` script:   ```bash
   python test_selenium.py   ```

2. The script will capture frames of a CSS animation and save them in the `frames` directory.

## Configuration

- **Stable Diffusion Prompt**: Modify the `prompt` variable in `auto_video_creator.py` to change the image generation prompt.
- **Frame Rate and Quality**: Adjust the `framerate` and `crf` parameters in the `create_video` function to change the video output settings.
- **CSS Animation**: Modify the `html_content` in `test_selenium.py` to change the animation.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Stable Diffusion](https://github.com/CompVis/stable-diffusion)
- [Selenium](https://www.selenium.dev/)
- [FFmpeg](https://ffmpeg.org/)
- [Torch](https://pytorch.org/)
- [PIL (Pillow)](https://python-pillow.org/)