import customtkinter as ctk
from pytubefix import YouTube
from tinydb import TinyDB, Query
from pathlib import Path
import os
from customtkinter import filedialog

db = TinyDB("Youtube.json")


# //////////////////////////////////////////////////////////////////
# //// Create A Popup function /////////////////////////
# //////////////////////////////////////////////////////////////////
def file(self):
    self.my_file = filedialog.askopenfilename(
        initialdir="",
        title="Select A File",
        filetypes=(("txt files", "*.txt"), ("All Files", "*.*")),
    )
    if self.my_file:
        self.my
# ///////////////////////////

def path_to_download(value):
    path_to_download = str(os.path.join(Path.home(), "Downloads"))
    save_path = path_to_download
    return save_path


def entry_input(my_entry, listBox):
    try:
        # Assuming URL is a valid YouTube URL
        # value = YouTube(URL)  # Create an instance of YouTube
        # name = value.title  # Get the title of the video
        # filename = ""  # Initialize filename
        # filename += name  # Concatenate the title to filename

        # # Download the first progressive stream with mp4 extension
        # value.streams.filter(progressive=True, file_extension="mp4").first().download(
        #     output_path=path_to_download(value=filename),  # Corrected to use a comma
        #     filename=filename,  # Use the filename variable
        # )
        URL = my_entry.get()
        value = URL
        listBox.insert("end", value)  # Add the value to the end of the listbox
    except Exception as e:
        print(f"Some Error! {e}")
        print("Task Completed!")
    # URL = my_entry.get()
    # value = (
    #     YouTube(URL)
    #     .streams.first()
    #     .download()
    #     .filter(progressive=True, file_extension="mp4")
    # )

    # entry.delete(0, 'end')  # Clear the entry after adding


# Removing method
def remove_entry(listBox):
    listBox.delete(0, "END")


def checkbox_event(x):
    # Access the value of the associated variable directly
    current_value = x.get()  # Assuming check_var is accessible here
    if current_value == 1:
        print("Checkbox toggled, current value: ", current_value)
    else:
        print("Checkbox is off, current value: ", current_value)
