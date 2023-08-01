import os
import random
import time
from moviepy.editor import VideoFileClip
import subprocess
import datetime

def get_video_duration(file_path):
    try:
        video = VideoFileClip(file_path)
        duration = video.duration
        video.close()
        return duration
    except Exception as e:
        print(f"Error while getting video duration: {str(e)}")
        return None

def is_night_time():
    now = datetime.datetime.now().time()
    night_start = datetime.time(21, 0)  # 9 PM
    night_end = datetime.time(6, 51)   # 7:30 AM

    if night_start <= now or now <= night_end:
        return True
    return False

def play_random_video(folder_path, repeat=1):
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
    # Replace '/path/to/your/folder' with the path of your folder containing video files
    day_time_folder_path = r"F:\RetroTV\Music Video Channel\Daytime\Commercial"
    night_time_folder_path_commercial = r"F:\RetroTV\Music Video Channel\Night Time\Commercial"
    night_time_folder_path_shows = r'F:\RetroTV\Music Video Channel\Night Time\Shows'
    while True:
        if is_night_time():
            print("Playing random videos from the night time folder:")
            play_random_video(night_time_folder_path_commercial, repeat = 1)
            #play_random_video(night_time_folder_path_shows, repeat = 1)
        else:
            print("Playing random videos from the day time folder:")
            for _ in range(2):
                play_random_video(day_time_folder_path, repeat=1)
