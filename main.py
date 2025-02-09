# from tkinter import *
import customtkinter as ctk
from CTkListbox import *
from functions import entry_input
from functions import checkbox_event

# window
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Grid")  # Use self to refer to the current instance
        self.geometry("700x500")
        # ////////////// Main Window Frame ///////////////
        self.my_frame = ctk.CTkFrame(
            master=self  # This is where am setting main frame to the root of the program
        )
        self.my_frame.grid()

        self.my_frame.grid_rowconfigure(
            0, weight=0
        )  # Here we have configured 2 rows to use
        self.my_frame.grid_rowconfigure(1, weight=1)
        self.my_frame.grid_columnconfigure(
            0, weight=1
        )  # Here we have configured 2 columns to use
        self.my_frame.grid_columnconfigure(1, weight=1)

        # Widgets
        self.label = ctk.CTkLabel(
            self.my_frame,
            text="Iam a Label",
        )
        self.button1 = ctk.CTkButton(self.my_frame, text="Button1")
        self.my_entry = ctk.CTkEntry(self.my_frame, width=500)

        self.x = ctk.IntVar()

        # Create the checkbox
        self.checkbox = ctk.CTkCheckBox(
            self.my_frame,
            text="CTkCheckBox",
            command=lambda: checkbox_event(self.x),
            variable=self.x,
            onvalue=1,
            offvalue=0,
        )
        self.checkbox.grid()

        self.second_frame = ctk.CTkFrame(master=self)
        # Placing widgets using Grid
        self.label.grid(row=1, column=0, padx=10, pady=10)
        self.my_entry.grid(row=2, column=0, padx=10, pady=10)
        self.checkbox.grid(row=2, column=1, padx=20, pady=10)
        self.button1.grid(row=3, column=0, padx=10, pady=10)
        self.second_frame.grid(row=0, column=2, sticky=("N", "S", "E"))

        # ////////////// List Box frame ///////////////


if __name__ == "__main__":
    app = App()
    # This runs the app
    app.mainloop()

# Build 2 frames
