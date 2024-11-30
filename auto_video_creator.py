import os
import time
import subprocess
from datetime import datetime
from diffusers import StableDiffusionPipeline
import torch
from PIL import Image

def generate_frames(pipe, prompt, num_frames, output_dir, width=1080, height=1920):
    """
    Generate images using Stable Diffusion based on the provided prompt.
    
    Args:
        pipe (StableDiffusionPipeline): The diffusion pipeline.
        prompt (str): Text prompt for image generation.
        num_frames (int): Number of frames to generate.
        output_dir (str): Directory to save generated frames.
        width (int, optional): Width of the images. Defaults to 1080.
        height (int, optional): Height of the images. Defaults to 1920.
    """
    os.makedirs(output_dir, exist_ok=True)
    
    for i in range(num_frames):
        print(f"Generating frame {i+1}/{num_frames}...")
        image = pipe(prompt, height=height, width=width).images[0]
        image.save(os.path.join(output_dir, f"frame_{i:05d}.png"))
        # Optional: Adjust sleep time if needed
        time.sleep(0.1)  # Short pause between frame generations

def create_video(output_dir, output_video, framerate=30, crf=20):
    """
    Compile generated frames into a video using FFmpeg.
    
    Args:
        output_dir (str): Directory containing image frames.
        output_video (str): Name of the output video file.
        framerate (int, optional): Frame rate for the video. Defaults to 30.
        crf (int, optional): Constant Rate Factor for quality. Defaults to 20.
    """
    ffmpeg_command = [
        'ffmpeg',
        '-y',  # Overwrite without asking
        '-framerate', str(framerate),
        '-i', os.path.join(output_dir, 'frame_%05d.png'),
        '-c:v', 'libx264',
        '-pix_fmt', 'yuv420p',
        '-vf', f'scale=1080:1920',
        '-crf', str(crf),
        output_video
    ]
    
    print("Creating video with FFmpeg...")
    subprocess.run(ffmpeg_command, check=True)
    print(f"Video saved as {output_video}")

def clean_up(output_dir):
    """
    Remove all files in the specified directory.
    
    Args:
        output_dir (str): Directory to clean up.
    """
    for file in os.listdir(output_dir):
        file_path = os.path.join(output_dir, file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")

def main():
    # Initialize Stable Diffusion pipeline
    model_id = "runwayml/stable-diffusion-v1-5"
    device = "cuda" if torch.cuda.is_available() else "cpu"
    
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16 if device == "cuda" else torch.float32)
    pipe = pipe.to(device)
    
    prompt = "A dog walking in a park during sunset, high resolution, 9:16 aspect ratio"
    
    while True:
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        output_dir = f"frames_{timestamp}"
        output_video = f"output_{timestamp}.mp4"
        
        try:
            # Generate frames
            generate_frames(pipe, prompt, num_frames=60, output_dir=output_dir)
            
            # Create video from frames
            create_video(output_dir, output_video, framerate=30, crf=20)
            
        except Exception as e:
            print(f"An error occurred: {e}")
        
        finally:
            # Clean up frames to save disk space
            clean_up(output_dir)
            print("Cleaned up frames.\n")
        
        # Optional: Wait before generating the next video
        wait_time = 60  # seconds
        print(f"Waiting for {wait_time} seconds before creating the next video...\n")
        time.sleep(wait_time)

if __name__ == "__main__":
    main()