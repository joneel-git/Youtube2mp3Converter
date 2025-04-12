from pytubefix import YouTube
from pathlib import Path
from CTkMessagebox import CTkMessagebox
import os, sys, threading, time, subprocess


class MyClass:
    def __init__(self, progressbar_widget):
        self.progressbar_widget = progressbar_widget
        self.downloads_path = Path.home() / "Downloads"
        self.check = os.name

    def path_to_images(self, image):
        # Step 1 get the path to images
        self.images_dir = Path.cwd() / "images" / image
        # Step 2 define image files and open them
        image = self.images_dir
        print(image)
        return image

    def error_message(self, error):
        CTkMessagebox(
            title="Error",
            message=f"Nope an error . {error}",
            icon=self.path_to_images("error.png"),
        )

    def success_message(self, success):
        CTkMessagebox(
            title="Success",
            message=f"Congratulations you did it. {success}",
            icon=self.path_to_images("check.png"),
        )

    # Trying to define Downloads Path TODO """

    def download_path(self):
        return self.downloads_path

    # Open Downloads Folder TODO """

    def open_downloads_path(self):
        if self.check == "posix":  # 'posix' is used for Linux and MacOS
            isLinux = subprocess.run(["open", f"{self.downloads_path}"], check=True)
            print("Yes, this is Linux or MacOS")
            return isLinux
        elif self.check == "nt":  # 'nt' is used for Windows
            isWindows = os.startfile(self.download_path())
            print("No, this is Windows")
            return isWindows
        else:
            print("Unsupported OS")

    # Add/Download file to list TODO """

    def video_Info(self, entry_widget, listbox_widget):
        try:
            URL = entry_widget.get()
            yt = YouTube(URL)  # Create Youtube Object.
            print("Title : ", yt.title)
            print("Total Length : ", yt.length, " Seconds")
            print("Total Views : ", yt.views)
            print("Is Age Restricted : ", yt.age_restricted)
            # print("Video Rating ", round(yt.rating))
            print("Thumbnail Url : ", yt.thumbnail_url)
            listbox_widget.insert("end", yt.title, yt.author)
            return self.success_message(success=yt)
        except Exception as e:
            self.error_message(e)

    # call the function
    # video_info(yt)

    # Remove file from list TODO """

    def remove_entry(self, listbox_widget):
        listbox_widget.delete(0, "END")

    # Implement progressbar TODO """

    def progress_the_bar(self):
        print("Are we even talking to the widget")
        try:
            self.progressbar_widget.step(10)
            print("Progress bar stepped by 10")
        except Exception as e:
            print(f"Error updating progress bar: {e}")

    # Checkbox event TODO """

    def checkbox_event(self, is_checked):
        # Access the value of the associated variable directly
        current_value = is_checked.get()  # This will work now
        if current_value == 1:
            print("Checkbox is on, current value: ", current_value)
        else:
            print("Checkbox is off, current value: ", current_value)
