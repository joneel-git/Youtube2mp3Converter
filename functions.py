from pytubefix import YouTube
from pathlib import Path
import os, sys, threading, time, subprocess


class MyClass:
    def __init__(self, progressbar_widget):
        self.progressbar_widget = progressbar_widget
        self.downloads_path = str(Path.home() / "Downloads")
        self.check = os.name

    # ///////////////////////////////////////////
    # //// Get Downloads Path //////////////////
    # ///////////////////////////////////////////
    # Computes and returns the file path to the user's Downloads directory.
    def download_path(self):
        return self.downloads_path

    # ///////////////////////////////////////////
    # //// Open Downloads Folder ///////////////
    # ///////////////////////////////////////////
    # Performs an action: opens the Downloads folder in the file explorer.
    # This method does not return a value.
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

        # subprocess.Popen(self.downloads_path)

    # ///////////////////////////////////////////
    # / Add/Download file to list TODO /////////
    # //////////////////////////////////////////

    # ///////////////////////////////////////////
    # //// Remove file from list TODO ///////////
    # ///////////////////////////////////////////
    # Removing method
    def remove_entry(listbox_widget):
        listbox_widget.delete(0, "END")

    # ///////////////////////////////////////////
    # //// Implement progressbar TODO ///////////
    # ///////////////////////////////////////////
    #  Action function rather than compute and return function
    def progress_the_bar(self):
        print("Are we even talking to the widget")
        try:
            self.progressbar_widget.step(10)
            print("Progress bar stepped by 10")
        except Exception as e:
            print(f"Error updating progress bar: {e}")

    # ///////////////////////////////////////////
    # //// Checkbox event TODO /////////////////
    # ///////////////////////////////////////////
    # @staticmethod
    def checkbox_event(self, is_checked):
        # Access the value of the associated variable directly
        current_value = is_checked.get()  # This will work now
        if current_value == 1:
            print("Checkbox is on, current value: ", current_value)
        else:
            print("Checkbox is off, current value: ", current_value)


# def download_video(self, entry_widget, listbox_widget):
#     value = self.

#     # Start the download in a new thread
#     threading.Thread(target=download).start()
