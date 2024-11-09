import customtkinter
from pytube import YouTube
from pytubefix import YouTube
from pytubefix.cli import on_progress
import requests

# System settings
customtkinter.set_appearance_mode("dark") # Modes: system (default), light dark
customtkinter.set_default_color_theme("dark-blue") # Themes: blue (default), dark

# Our app frame
app = customtkinter.CTk()
app.title("Youtube to mp3 converter")
app.geometry("700x450")

# Adding Ui Elements
my_font = customtkinter.CTkFont(family="Helvetica", size=22)

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
    width=150,
    height=30,
    border_width=2,
    corner_radius=5
)
entry.pack()

# This is our callback function
def get_entry_value():
    try:
        url = entry.get()
        yt = YouTube(url, on_progress_callback=on_progress)
        print(yt.title)
        ys = yt.streams.get_highest_resolution()
        ys = yt.streams.get_audio_only()
        ys.download(mp3=True)
        print("Download is completed successfully")  # Print success message
    except Exception as e:
        print(f"An error has occurred: {e}")  # Print error message

# This is the button Widget to handle an event 
MyButton1 = customtkinter.CTkButton(app, text="Download video", 
    font=my_font,
    width=40, height=20, command=get_entry_value)
MyButton1.pack(padx=20, pady=20)

# A button to clear the entry widget
clear_button = customtkinter.CTkButton(app, text="clear")
clear_button.pack(padx=33, pady=33)
clear_button.configure(command=lambda: entry.delete(0, customtkinter.END))

titleLabel = customtkinter.CTkLabel(app, text=yt.title)
# Handle app closing
# Function to handle window closing
def on_closing():
    app.destroy()  # Close the application

# Set the protocol for window closing
app.protocol("WM_DELETE_WINDOW", on_closing)

# Run App
app.mainloop()

# TODO how to share information between widgets ??? 
# yt.title to pack to the app frame instead of print