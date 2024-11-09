from tkinter import *
import customtkinter
from pytube import YouTube
import requests
from bs4 import BeautifulSoup
import os
import subprocess

# System settings
customtkinter.set_appearance_mode("dark") # Modes: system (default), light dark
customtkinter.set_default_color_theme("dark-blue") # Themes: blue (default), dark

# Our app frame
app = customtkinter.CTk()
app.title("Youtube to mp3 converter")
app.geometry("700x450")

# Adding Ui Elements
my_font = customtkinter.CTkFont(family="Helvetica", size=22)

my_label = customtkinter.CTkLabel(app, 
    text="Enter a Youtube URL: ", 
    text_color="white", 
    font=my_font
    )
my_label.pack(pady=50, padx=30)

entry = customtkinter.CTkEntry(master=app,
    placeholder_text="link",
    font=my_font,
    width=150,
    height=30,
    border_width=2,
    corner_radius=5
)
entry.pack()

# How do I get the Entry's value in tkinter?

# Link input

# This is the Entry Widget
def get_entry_value():
    link = entry.get()
    r = requests.get(link)
    soup = BeautifulSoup(r.text, "html.parser")
    link = soup.find_all(name="title")[0]
    title = str(link)
    title = title.replace("<title>", "")
    title = title.replace("</title>", "")
    print(title)
# This is the button Widget to handle an event 
MyButton1 = customtkinter.CTkButton(app, text="Download video", 
    font=my_font,
    width=40, height=20, command=get_entry_value)
MyButton1.pack(padx=20, pady=20)

# Handle app closing
# Function to handle window closing
def on_closing():
    app.destroy()  # Close the application

# Set the protocol for window closing
app.protocol("WM_DELETE_WINDOW", on_closing)

# Run App
app.mainloop()