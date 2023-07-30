import os
import random
import time
from moviepy.editor import VideoFileClip
import subprocess


def get_video_duration(file_path):
    try:
        video = VideoFileClip(file_path)
        duration = video.duration
        video.close()
        return duration
    except Exception as e:
        print(f"Error while getting video duration: {str(e)}")
        return None

def play_random_video(folder_path, repeat = int):
    # Get a list of video files in the folder
    video_extensions = [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm"]
    video_files = [file for file in os.listdir(folder_path) if file.lower().endswith(tuple(video_extensions))]

    if not video_files:
        print("No video files found in the specified folder.")
        return

    for _ in range(repeat):
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
        time.sleep(duration)


if __name__ == "__main__":
    # Replace 'folder_path' with the actual path of your folder
    original_folder_path = "F:\RetroTV\Music Video Channel\Daytime\Commercial"
    new_folder_path = "F:\RetroTV\Music Video Channel\Daytime\Commercial"
    while True:
        print("Playing videos from the original folder:")
        
        play_random_video(original_folder_path, 2)

        print("Playing videos from the new folder:")
        
        play_random_video(new_folder_path, 1)
