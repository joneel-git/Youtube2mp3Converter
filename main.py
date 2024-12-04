import customtkinter
from pytube import YouTube
from pytubefix import YouTube
from pytubefix.cli import on_progress
from CTkMessagebox import CTkMessagebox
from customtkinter import CTkButton, CTk
import os
import sys
import requests

# System settings
customtkinter.set_appearance_mode("dark") # Modes: system (default), light dark
customtkinter.set_default_color_theme("dark-blue") # Themes: blue (default), dark

# Our app frame
app = customtkinter.CTk()
app.title("Youtube to mp3 converter")
app.geometry("700x450")

# Adding Ui Elements
my_font = customtkinter.CTkFont(family="Helvetica", size=17)

# This is the main label
my_label = customtkinter.CTkLabel(app, 
    text="Enter a Youtube URL: ", 
    text_color="white", 
    font=my_font
    )
my_label.pack(pady=50, padx=30)

# This is our Entry Widget where we add the URL
entry = customtkinter.CTkEntry(master=app,
    placeholder_text="link",
    font=my_font,
    width=450,
    height=30,
    border_width=2,
    corner_radius=5
)
entry.pack(padx=33, pady=33)

# Create a CTkLabel instance for displaying download progress
download_label = customtkinter.CTkLabel(master=app, text="", width=12, height=12)
download_label.pack(padx=22, pady=22)

# checking resource path tha we have our icons
def resource_path(relative_path):
    """ Get the absolute path to the resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# This is our callback function
def get_entry_value():
    url = entry.get()  # Assuming you have an entry widget to get the URL
    try:
        # This is the Actual youtube object
        yt = YouTube(url, on_progress_callback=on_progress)

        # Attempt to get highest resolution video or audio only
        ys = yt.streams.get_highest_resolution() or yt.streams.get_audio_only()
        
        # Download and save as .mp3
        ys.download(filename=yt.title + ".mp3")
        # TODO display the downloading progress in the gui
        download_label.configure(text=f"Downloading: {yt.title}")
        # Clear the on_progress_callback
        yt.on_progress_callback = None
        
        # Show success message
        CTkMessagebox(title="Success", message="Download completed successfully!", icon=resource_path("check.png"))
        
    except Exception as e:
        # Show error message
        CTkMessagebox(title="Error", message=f"An error has occurred: {e}", icon=resource_path("error.png"))


# This is the button Widget to handle an event 
MyButton1 = customtkinter.CTkButton(app, text="Convert to mp3", 
    font=my_font,
    width=40, height=20, command=get_entry_value)
MyButton1.pack(padx=20, pady=30)

# A button to clear the entry widget
clear_button = customtkinter.CTkButton(app, text="clear")
clear_button.pack(padx=33, pady=10)
clear_button.configure(command=lambda: (entry.delete(0, customtkinter.END), download_label.configure(text="")))
# download_label.configure(text="")
# Handle app closing
# Function to handle window closing
def on_closing():
    app.destroy()  # Close the application
    app.quit()     # Ensure the program exits completely

# Set the protocol for window closing
app.protocol("WM_DELETE_WINDOW", on_closing)

# Run App
app.mainloop()
