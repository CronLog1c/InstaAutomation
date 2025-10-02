import os
import time
from datetime import datetime
from instagrapi import Client
import config

#Add the folder where you downloaded videos too. Or just any folder thats holding videos.

VIDEO_FOLDER = r""
VIDEO_EXTENSIONS = ('.mp4', '.mov', '.avi', '.mkv')

def countdown(seconds):
    for remaining in range(seconds, 0, -1):
        mins, secs = divmod(remaining, 60)
        time_str = f"{mins:02}:{secs:02}"
        print(f"\rNext upload in: {time_str}", end="", flush=True)
        time.sleep(1)
    print("\rUploading next video....           ")

cl = Client()
cl.login(config.username, config.password)
print("Logged into Instagram successfully.")

video_files = [f for f in os.listdir(VIDEO_FOLDER) if f.lower().endswith(VIDEO_EXTENSIONS)]

if not video_files:
    print("No video files found to upload.")
else:
    for index, filename in enumerate(video_files):
        video_path = os.path.join(VIDEO_FOLDER, filename)
        print(f"Uploading video: {filename}")

        try:
            media = cl.video_upload(
                path=video_path,
                caption="Follow me (@arch1vr) #memes #follow #like"
            )
            media_id = getattr(media, "pk", None) or getattr(media, "id", None)
            print(f"Successfully uploaded: {filename} (media ID: {media_id})")

        except Exception as e:
            print(f"Failed to upload {filename}: {e}")
        # I had it wait 20 mins since I would get rate limited on instagram. You can change this if you want. Be careful because it will upload every single video in the folder stupid fast.
        if index < len(video_files) - 1:
            print(f"Waiting 20 minutes before next upload.")
            countdown(20 * 60)
        else:
            print("All videos uploaded.")
