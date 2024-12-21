from pytube import YouTube
from pytubefix import YouTube
from pytubefix.cli import on_progress
from CTkMessagebox import CTkMessagebox
from customtkinter import CTkButton, CTk


def get_url_from(entry):
    save_path = "C:/Users/joneel/Downloads/"
    url = entry.get()  # Get the URL from the entry widget
    try:
        # This is the youtube object
        yt = YouTube(url)
        # Attempt to get highest resolution video or audio only
        ys = yt.streams.get_audio_only()
        ys.download(output_path=save_path)

        CTkMessagebox(
            title="Success",
            message="Download completed successfully!",
            icon="images\\check.png",  # Ensure this is the correct way to specify the icon
        )
        # Select download location for youtube video
        return ys

    except Exception as e:
        CTkMessagebox(
            title="Error",
            message=f"An error has occurred: {e}",
            icon="images\\error.png",
        )
        return None

    # # Show success message
    # CTkMessagebox(
    #     title="Success",
    #     message="Download completed successfully!",
    #     icon="check.png",  # Ensure this is the correct way to specify the icon
    # )


# CTkMessagebox(
#     title="Error",
#     message=f"An error has occurred: {e}",
#     icon="error.png",
# )
