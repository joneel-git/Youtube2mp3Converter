from customtkinter import *
from CTkListbox import *
from functions import *
from layout import *


# Define a class that inherits from CTk, which is the main window class in tkinter
class Main_container(CTk, Functions):
    def __init__(self):
        super().__init__()  # Call the initializer of the parent class (CTk)
        self.title("My Tkinter App")
        self.geometry("800x600")

        # Create all widgets
        self.label_widget = CTkLabel(self, text="I am a Label")
        self.listbox_widget = CTkListbox(
            self, border_color="gray", border_width=1, width=500, height=200
        )
        self.entry_widget = CTkEntry(self, width=500)

        # Button to submit data
        self.submit_widget = CTkButton(
            self,
            command=self.submit_data,
            text="Submit",
        )

        self.progressbar_widget = CTkProgressBar(self)

        self.remove_widget = CTkButton(
            self,
            command=self.remove_entry,
            text="Remove Entry",
        )

        # File dialog method
        self.my_text_widget = CTkLabel(
            self, text_color="green", width=100, height=70, text="File dialog"
        )
        self.browsefile_widget = CTkButton(
            self,
            width=10,
            height=10,
            command=self.open_downloads_path, 
            text="Browse file",
        )

        # Checkbox state
        self.is_checked = IntVar()
        self.checkbox_widget = CTkCheckBox(
            self,
            text="CTkCheckBox",
            command=self.checkbox_event,
            variable=self.is_checked,
            onvalue=1,
            offvalue=0,
        )

        # Layout the widgets using the function from layout.py
        Layout_widgets.layout_widgets(self)


# Create an instance of the Main_container class, which initializes the Tkinter window
if __name__ == "__main__":
    container = Main_container()
    container.mainloop()
