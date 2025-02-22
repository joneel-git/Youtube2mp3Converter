import customtkinter as ctk
from pytube import YouTube
from tinydb import TinyDB, Query

db = TinyDB("Youtube.json")


def entry_input(my_entry, my_list):
    # YoutubeObjects = (
    #     YouTube(URL)
    #     .streams.first()
    #     .download()
    #     .filter(progressive=True, file_extension="mp4")
    # )
    value = my_entry.get()  # Get the input from the CTkEntry
    my_list = [value]
    if my_list:  # Check if the input is not empty
        db.insert({"entry": my_list})  # Insert the input into the database
        # my_list.insert("end", collectdata)  # Add the input to the CTkListBox
        print(db)


# Removing method
def remove_entry(my_list):
    for x in my_list:
        db.remove(x)


def checkbox_event(x):
    # Access the value of the associated variable directly
    current_value = x.get()  # Assuming check_var is accessible here
    if current_value == 1:
        print("Checkbox toggled, current value: ", current_value)
    else:
        print("Checkbox is off, current value: ", current_value)
