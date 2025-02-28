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
        self.label = ctk.CTkLabel(
            master=self,
            text="Iam a Label",
        )
        # //////////
        self.listBox = CTkListbox(
            master=self,
            border_color="gray",
            border_width=1,
            width=500,
            height=200,
        )
        # //////// the Entry widget
        self.my_entry = ctk.CTkEntry(master=self, width=500)

        # //////// This button sends data from my_entry to my_list widget
        self.button1 = ctk.CTkButton(
            master=self,
            command=lambda: entry_input(self.my_entry, self.listBox),
            text="Submit",
        )

        self.button2 = ctk.CTkButton(
            master=self,
            command=lambda: remove_entry(self.listBox),
            text="Remove",
        )
        # //////////////////////////////////////////////////////////////////
        # //// Am working on File dialog method here /////////////////////////
        # //////////////////////////////////////////////////////////////////
        self.my_text = ctk.CTkTextbox(master=self, width=100, height=70)
        self.add_value = ctk.CTkButton(
            master=self,
            # command=lambda: entry_input(self.my_entry, self.listBox),
            text="add_value",
        )
        # ///////////////////////

        self.x = ctk.IntVar()

        # Create the checkbox
        self.checkbox = ctk.CTkCheckBox(
            master=self,
            text="CTkCheckBox",
            command=lambda: checkbox_event(self.x),
            variable=self.x,
            onvalue=1,
            offvalue=0,
        )
        self.checkbox.grid()

        # Placing widgets using Grid
        self.label.grid(row=1, column=0, padx=10, pady=10)
        self.checkbox.grid(row=2, column=2, padx=10, pady=10)
        self.button1.grid(row=3, column=0, padx=10, pady=10)
        self.button2.grid(row=3, column=1, sticky="w")
        # //////////////////////////////////////////////////////////////////
        # //// Am working on File dialog method here /////////////////////////
        # //////////////////////////////////////////////////////////////////
        self.add_value.grid(row=4, column=0, padx=10, pady=10)
        self.my_text.grid(row=4, column=1, padx=10, pady=10,sticky="w")
        # ///////
        self.my_entry.grid(row=2, column=0, padx=10, pady=10, columnspan=2)
        self.listBox.grid(row=5, column=0, padx=20, pady=20, sticky="ew", columnspan=2)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Grid")  # Use self to refer to the current instance
        self.geometry("700x500")
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
