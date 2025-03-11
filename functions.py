import customtkinter as ctk
from pytubefix import YouTube
from pytubefix import *
from tinydb import TinyDB, Query
from pathlib import Path
import threading
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


def download_path():
    downloads_path = str(Path.home() / "Downloads")
    save_path = downloads_path 
    return save_path


def download_video(entry_widget, listbox_widget):
    def download():
        try:
            my_input = entry_widget.get()
            youtube = YouTube(my_input.strip())
            filename = youtube.title
            youtube.streams.get_highest_resolution().download(
                output_path=download_path()
            )

            listbox_widget.insert("end", filename)  # Insert the value into the Listbox
            print(filename)  # Print the title of the video
        except Exception as e:
            print(f"Some Error! {e}")  # Print the error message

    # Start the download in a new thread
    threading.Thread(target=download).start()



# Removing method
def remove_entry(listbox_widget):
    listbox_widget.delete(0, "END")


def checkbox_event(checkbox_state):
    # Access the value of the associated variable directly
    current_value = checkbox_state.get()  # Assuming check_var is accessible here
    if current_value == 1:
        print("Checkbox is on, current value: ", current_value)
    else:
        print("Checkbox is off, current value: ", current_value)
