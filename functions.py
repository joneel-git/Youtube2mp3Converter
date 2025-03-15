from pytubefix import YouTube
from pathlib import Path
import threading
import os

# class MyClass(object):
#     def __init__(self):
#         self.a = ['A','X','R','N','L']  # Shared instance member :D

#     def fun1(self, string):
#         out = []
#         for letter in self.a:
#             out.append(string+letter)
#         return out

#     def fun2(self, number):
#         out = []
#         for letter in self.a:
#             out.append(str(number)+letter)
#         return out

# a = MyClass()
# x = a.fun1('Hello ')
# y = a.fun2(2)
class MyClass(object):
    def __init__(self):
        pass  # You can initialize any instance variables here if needed

    def download_video(self, entry_widget, listbox_widget):
        def download():
            try:
                self.url = entry_widget.get().strip()  # Get the URL from the entry widget
                yt = YouTube(self.url)  # Create a YouTube object
                self.filename = f"{yt.title} - {yt.author}"  # Use f-string for filename
                self.file_path = download_path(file=self.filename)  # Define your download_path function
                # Check if the file already exists
                self.has_file = os.path.exists(self.file_path)
                if self.has_file:
                    print("The file exists.")
                    listbox_widget.insert("end", f"The file '{self.filename}' already exists.")
                else:
                    # Download the video
                    yt.streams.get_highest_resolution().download(output_path=self.file_path)
                    listbox_widget.insert("end", self.filename)  # Insert the value into the Listbox
                    print(f"Downloaded: {self.filename}")  # Print the title of the video
            except Exception as e:
                print(f"Some Error! {e}")  # Print the error message
                listbox_widget.insert("end", f"Error: {e}")  # Insert the error message into the Listbox

        # Start the download in a new thread
        threading.Thread(target=download).start()



def download_path(file):
    downloads_path = str(Path.home() / "Downloads")
    file = downloads_path
    return file 

# def file_exists():
# ///////////////////////////

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
