import os
from pathlib import Path


class Functions:
    def __init__(self):
        pass  # Constructor method, currently does nothing

    def attributes(self, entry_widget, listbox_widget, downloads_path, check):
        # Store references to the provided widgets and paths for later use
        self.downloads_path = downloads_path
        self.check = check
        self.entry_widget = entry_widget
        self.listbox_widget = listbox_widget

    def submit_data(self):
        # Retrieve input from the entry widget
        get_input = self.entry_widget.get()
        print("Getting input:", get_input)  # Log the retrieved input
        if get_input:  # Check if input is not empty
            self.listbox_widget.insert("end", get_input)  # Add input to the listbox
        else:
            print("Couldn't retrieve input; something went wrong.")  # Log error if input is empty

    def remove_entry(self):
        # Placeholder for logic to remove an entry from the listbox
        print("Entry removed!")  # Log that an entry has been removed

    def open_downloads_path(self):
        # Set downloads_path to the user's Downloads directory
        self.downloads_path = str(Path.home() / "Downloads")
        print("Opened downloads path:", self.downloads_path)  # Log the downloads path
        self.check = os.name  # Store the name of the operating system
        print("Checking OS:", str(self.check))  # Log the OS name

