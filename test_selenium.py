from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import os
import torch
import torchvision.transforms as transforms
from PIL import Image

# Setup Chrome options (headless mode)
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run without opening the browser window
chrome_options.add_argument("--no-sandbox")  # For Linux compatibility
chrome_options.add_argument("--disable-gpu")  # Disable GPU for compatibility

# Update the path to the Chrome binary on your Desktop
chrome_options.binary_location = "/Users/jakub/Desktop/Google Chrome.app/Contents/MacOS/Google Chrome"

# Specify the location of chromedriver (if not in PATH)
service = Service("/usr/local/bin/chromedriver")

# Initialize the webdriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Create a simple HTML page with a CSS animation (inline)
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=1080, initial-scale=1.0">
    <title>CSS Animation</title>
    <style>
        /* Define the keyframe animation */
        @keyframes moveTitle {
            0% {
                left: 0;
                color: red;
            }
            100% {
                left: 100%;
                color: blue;
            }
        }

        /* Apply the animation to an element */
        .animated-title {
            position: absolute;
            font-size: 150px;
            animation: moveTitle 5s linear infinite;
        }

        body {
            margin: 0;
            width: 1080px;
            height: 1920px;
            background-color: #000;
            overflow: hidden;
            position: relative;
        }
    </style>
</head>
<body>
    <div class="animated-title">Hello, CSS Animation!</div>
</body>
</html>
"""

# Save the HTML content to a temporary file
html_file_path = "/tmp/animation.html"
with open(html_file_path, "w") as f:
    f.write(html_content)

# Load the local HTML animation file
driver.get(f"file://{html_file_path}")

# Allow the animation to load for a short time before capturing frames
time.sleep(2)  # Increased delay to ensure animation starts

# Capture screenshots (60 frames per second for 1 second)
frame_count = 60  # Number of frames to capture
output_dir = "frames"
os.makedirs(output_dir, exist_ok=True)

# Define a transformation for image generation
transform = transforms.ToPILImage()

# Capture each frame of the animation
for i in range(frame_count):
    # Generate a random image tensor with YouTube Shorts resolution
    generated_image = torch.randn(3, 1920, 1080)  # 3 channels (RGB), 1080x1920

    # Normalize the tensor to 0-1 range
    generated_image = (generated_image - generated_image.min()) / (generated_image.max() - generated_image.min())

    # Convert the tensor to a PIL image
    image = transform(generated_image)

    # Save the image
    image.save(f"{output_dir}/frame_{i:03d}.png")

    time.sleep(1 / 60)  # Wait for the next frame (for 60 FPS)

# Close the browser
driver.quit()

print(f"Captured {frame_count} frames in YouTube Shorts format!")
