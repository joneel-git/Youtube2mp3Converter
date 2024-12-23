from pytube import YouTube
from pytubefix import YouTube
from pytubefix.cli import on_progress
from CTkMessagebox import CTkMessagebox
from customtkinter import CTkButton, CTk
from pathlib import Path
import os


def path_to_images(image_name):
    # Get the current working directory
    image_dir = os.getcwd()
    # The full path to the image
    images_path = os.path.join(image_dir, "images", image_name)
    return images_path


def get_url_from(entry):
    path_to_download = str(os.path.join(Path.home(), "Downloads"))
    save_path = path_to_download
    url = entry.get()  # Get the URL from the entry widget
    try:
        # This is the youtube object
        yt = YouTube(url)
        # Attempt to get highest resolution video or audio only
        ys = yt.streams.filter(only_audio=True).first()
        # Set the filename to the video title with .mp3 extension
        filename = f"{yt.title}.mp3"
        # Download the audio stream
        ys.download(output_path=save_path, filename=filename)

        CTkMessagebox(
            title="Success",
            message="Download completed successfully!",
            icon=path_to_images("check.png"),
        )
        return ys

    except Exception as e:
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
