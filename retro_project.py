import os
import random
import time
from moviepy.editor import VideoFileClip
import subprocess
import glob

def get_video_duration(file_path):
    try:
        video = VideoFileClip(file_path)
        duration = video.duration
        video.close()
        return duration
    except Exception as e:
        print(f"Error while getting video duration: {str(e)}")
        return None

def play_random_video(folder_path):
    # Get a list of video files in the folder
    video_extensions = [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm"]
    video_files = [file for file in os.listdir(folder_path) if file.lower().endswith(tuple(video_extensions))]

    if not video_files:
        print("No video files found in the specified folder.")
        return

    while True:
        # Randomly select a video file from the list
        random_video = random.choice(video_files)

        # Get the full path to the video file
        video_path = os.path.join(folder_path, random_video)

        # Get the video duration
        duration = get_video_duration(video_path)
        if duration is None:
            continue

        # Open the selected video file
        try:
            print(f"Playing random video from {folder_path}: {random_video}")
            subprocess.Popen(["explorer", video_path])  # This will open the video using the default application
        except Exception as e:
            print(f"Error opening the video: {str(e)}")
            continue

        # Wait until the video ends
        print(duration)
        time.sleep(duration)
        
    
        print('getting new video folder')

        # Choose a new folder and play one random video
        new_folder = "F:\RetroTV\Music Video Channel\Daytime\Shows\Retro Music Video"
        video_files_in_new_folder = glob.glob(os.path.join(new_folder, "*"))
        if not video_files_in_new_folder:
            print("No video files found in the new folder.")
            break

        random_video = random.choice(video_files_in_new_folder)
        duration = get_video_duration(random_video)
        print(duration)
        if duration is None:
            continue
        try:
            print(f"Playing random video from the new folder: {os.path.basename(random_video)}")
            subprocess.Popen(["explorer", random_video])
        except Exception as e:
            print(f"Error opening the video: {str(e)}")
            break
        time.sleep(duration)

if __name__ == "__main__":
    # Replace 'folder_path' with the actual path of your folder
    folder_path = "F:\RetroTV\Music Video Channel\Daytime\Commercial"

    play_random_video(folder_path)
