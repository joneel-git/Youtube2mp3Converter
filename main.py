# from tkinter import *
import customtkinter as ctk
from CTkListbox import *
from functions import *

# window
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


class MyFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Widgets..
        self.label_widget = ctk.CTkLabel(
            master=self,
            text="Iam a Label",
        )
        # //////////
        self.listbox_widget = CTkListbox(
            master=self,
            border_color="gray",
            border_width=1,
            width=500,
            height=200,
        )
        self.entry_widget = ctk.CTkEntry(master=self, width=500)
        # //////// This button sends data from my_entry to my_list widget
        my_class_instance = MyClass() # Initialize instance of the class

        self.submit_widget = ctk.CTkButton(
            master=self,
            command=lambda: my_class_instance.download_video(self.entry_widget, self.listbox_widget),
            text="Submit",
        )

        self.remove_widget = ctk.CTkButton(
            master=self,
            command=lambda: remove_entry(self.listbox_widget),
            text="Remove",
        )
        # //////////////////////////////////////////////////////////////////
        # //// Am working on File dialog method here /////////////////////////
        # //////////////////////////////////////////////////////////////////
        self.my_text_widget = ctk.CTkLabel(
            master=self,
            text_color="green",
            width=100,
            height=70,
            text="file dialog",
        )

        self.progressbar_widget = ctk.CTkProgressBar(master=self)
        # self.progressbar_widget = ctk.CTkProgressBar(master=self, mode="indeterminate")

        self.browsefile_widget = ctk.CTkButton(
            master=self,
            width=10,
            height=10,
            # command=lambda: progressbar_logic(self.progressbar_widget),
            text="Browse file",
        )
        # This name indicates that the variable holds the state of the checkbox (checked or unchecked).
        self.checkbox_state = ctk.IntVar()

        # Create the checkbox
        self.checkbox_widget = ctk.CTkCheckBox(
            master=self,
            text="CTkCheckBox",
            command=lambda: checkbox_event(self.checkbox_state),
            variable=self.checkbox_state,
            onvalue=1,
            offvalue=0,
        )
        self.checkbox_widget.grid()

        # Placing widgets using Grid
        # Row 0: Label
        self.label_widget.grid(row=0, column=0, padx=10, pady=10, columnspan=3)
        # Row 1: Progress Bar
        self.progressbar_widget.grid(
            row=1, column=0, padx=30, pady=30, columnspan=2, sticky="ew"
        )
        # Row 2: Entry Widget
        self.entry_widget.grid(row=2, column=0, padx=10, pady=10, columnspan=3)
        # Row 3: Checkbox (align to right in column 3)
        self.checkbox_widget.grid(row=3, column=3, padx=10, pady=10, sticky="e")
        # Row 3: Buttons (span columns for better alignment)
        self.submit_widget.grid(row=3, column=0, padx=10, pady=10)
        self.remove_widget.grid(row=3, column=1, padx=10, pady=10)
        self.listbox_widget.grid(
            row=5, column=0, padx=20, pady=20, sticky="ew", columnspan=2
        )
        self.browsefile_widget.grid(row=4, column=0, padx=10, pady=10)
        self.my_text_widget.grid(row=4, column=1, padx=10, pady=10, sticky="w")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Grid")  # Use self to refer to the current instance
        self.geometry("700x570")
        # This is placing the class MyFrame above on to the root of the app
        self.my_frame = MyFrame(master=self)
        self.my_frame.grid()
        self.my_frame.grid_rowconfigure(0, weight=0)
        self.my_frame.grid_rowconfigure(1, weight=1)
        self.my_frame.grid_columnconfigure(0, weight=1)
        self.my_frame.grid_columnconfigure(1, weight=1)


if __name__ == "__main__":
    app = App()
    # This runs the app
    app.mainloop()
