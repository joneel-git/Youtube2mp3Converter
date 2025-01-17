import re  
from pytube import YouTube 
import yt_dlp
import os
import sys
from pathlib import Path
from CTkMessagebox import CTkMessagebox


def path_to_images(image_name):
    # For PyInstaller, use _MEIPASS to get the path when bundled
    if hasattr(sys, '_MEIPASS'):
        image_dir = sys._MEIPASS
    else:
        image_dir = os.getcwd()
    
    # The full path to the image
    images_path = os.path.join(image_dir, "images", image_name)
    return images_path


def get_url_from(entry):
    print("Function called")
    path_to_download = str(os.path.join(Path.home(), "Downloads"))
    save_path = path_to_download
    url = entry.get()  # Get the URL from the entry widget
    print("URL:", url)

    # Validate the YouTube URL
    if not re.match(r"^(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+$", url):
        CTkMessagebox(
            title="Error",
            message="Please enter a valid YouTube URL.",
            icon=path_to_images("error.png"),
        )
        return None

    try:
        # Set options for yt-dlp
        ydl_opts = {
            "format": "bestaudio/best",
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
            "outtmpl": os.path.join(save_path, "%(title)s.%(ext)s"),
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        CTkMessagebox(
            title="Success",
            message="Download completed successfully!",
            icon=path_to_images("check.png"),
        )
        return None

    except Exception as e:
        print("Error occurred:", e)
        CTkMessagebox(
            title="Error",
            message=f"An error has occurred: {e}",
            icon=path_to_images("error.png"),
        )
        return None

    # # Show success message
    # CTkMessagebox(
    #     title="Success",
    #     message="Download completed successfully!",
    #     icon="check.png",
    # )


# CTkMessagebox(
#     title="Error",
#     message=f"An error has occurred: {e}",
#     icon="error.png",
# )
