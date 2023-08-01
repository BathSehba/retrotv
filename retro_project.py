import os
import random
import time
from moviepy.editor import VideoFileClip
import subprocess
import datetime
import sys
import msvcrt


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
    night_end = datetime.time(7, 30)   # 7:30 AM

    if night_start <= now or now <= night_end:
        return True
    return False

def choose_folder_path(channel, is_night):
    channels = {
        # 1 - Cartoons
        1: {
            True: r'F:\RetroTV\Cartoon Channel\Night Time\Shows\Beavis & Butt-Head (1993) S01 - S10\Season 1' or r'F:\RetroTV\Cartoon Channel\Night Time\Shows\Beavis & Butt-Head (1993) S01 - S10\Season 2',
            False: r"F:\RetroTV\Cartoon Channel\Daytime\Shows\Batman The Animated Series (1992) S01 - S04 + Extras\Season 1",
            "commercials": {
                True: r"F:\RetroTV\Cartoon Channel\Night Time\Commercial",
                False: r"F:\RetroTV\Cartoon Channel\Daytime\Commercial"
            }
        },
        # 2 - Movies
        2: {
            True: r"F:\RetroTV\Movie Channel\Night Time\Shows",
            False: r"F:\RetroTV\Movie Channel\Daytime\Shows",
            "commercials": {
                True: r"F:\RetroTV\Movie Channel\Night Time\Commercial",
                False: r"F:\RetroTV\Movie Channel\Daytime\Commercial"
            }
        },
        # 3 - Music Videos
        3: {
            True: r"F:\RetroTV\Music Video Channel\Night Time\Shows",
            False: r"F:\RetroTV\Music Video Channel\Daytime\Shows",
            "commercials": {
                True: r"F:\RetroTV\Music Video Channel\Night Time\Commercial",
                False: r"F:\RetroTV\Music Video Channel\Daytime\Commercial"
            }
        }
    }
    return channels[channel][is_night], channels[channel]["commercials"][is_night]

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

def play_commercial(commercial_folder, repeat=1):
    # Get a list of commercial video files in the folder
    video_extensions = [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm"]
    commercial_files = [file for file in os.listdir(commercial_folder) if file.lower().endswith(tuple(video_extensions))]

    if not commercial_files:
        print("No commercial video files found in the specified folder.")
        return

    for _ in range(repeat):
        # Randomly select a commercial video file from the list
        random_commercial = random.choice(commercial_files)

        # Get the full path to the commercial video file
        commercial_path = os.path.join(commercial_folder, random_commercial)

        # Get the commercial video duration
        duration = get_video_duration(commercial_path)
        if duration is None:
            continue

        # Open the commercial video file
        try:
            print(f"Playing commercial from {commercial_folder}: {random_commercial}")
            subprocess.Popen(["explorer", commercial_path])  # This will open the video using the default application
        except Exception as e:
            print(f"Error opening the commercial: {str(e)}")
            continue

        # Wait until the commercial ends
        time.sleep(duration)

def get_new_channel_choice():
    print("Waiting for new channel choice (3 seconds timeout)...")
    start_time = time.time()

    while True:
        if time.time() - start_time > 3:
            return None

        if msvcrt.kbhit():  # Check if a key has been pressed
            new_choice = msvcrt.getch().decode().strip()
            try:
                channel_choice = int(new_choice)
                if channel_choice in [1, 2, 3]:
                    return channel_choice
                else:
                    print("Invalid channel choice. Please enter a valid channel number (1, 2, 3).")
            except ValueError:
                print("Invalid input. Please enter a valid channel number (1, 2, 3).")

if __name__ == "__main__":
    channel_choice = int(input("Enter the channel number (1, 2, 3) (0 to exit): "))
    if channel_choice == 0:
        print("Exiting the script.")
    else:
        while True:
            is_night = is_night_time()
            print(f"The system time is {'night' if is_night else 'day'}.")
            
            folder_path, commercial_folder = choose_folder_path(channel_choice, is_night)
            if folder_path is None or commercial_folder is None:
                print("Invalid channel choice. Please choose a valid channel number.")
                continue
            
            print(f"Playing random videos from channel {channel_choice}: {folder_path}")
            for _ in range(1):
                play_random_video(folder_path, repeat=1)
            
            print(f"Playing commercials from channel {channel_choice}: {commercial_folder}")
            for _ in range(1):
                play_commercial(commercial_folder, repeat=1)

            # Ask the user if they want to change the channel
            new_channel_choice = get_new_channel_choice()
            if new_channel_choice is not None:
                channel_choice = new_channel_choice
            else:
                print("No new channel choice within the timeout. Repeating the loop with the current channel.")
