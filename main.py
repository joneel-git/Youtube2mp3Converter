from customtkinter import *
import customtkinter as ctk
from CTkListbox import *
from functions import MyClass  # Import MyClass directly

# Set appearance mode and color theme using public methods
ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme(
    "themes/teal.json"
)  # Themes: "blue" (standard), "green", "dark-blue"


class MyGUI:
    def __init__(self, master):
        self.master = master
        self.c = MyClass(self)  # Store MyClass instance

        self.create_widgets()  # Create widgets
        self.layout_widgets()  # Layout widgets

    def create_widgets(self):
        # Create all widgets
        self.label_widget = CTkLabel(self.master, text="I am a Label")
        self.listbox_widget = CTkListbox(
            self.master, border_color="gray", border_width=1, width=500, height=200
        )
        self.entry_widget = CTkEntry(self.master, width=500)

        # Button to submit data
        self.submit_widget = CTkButton(
            self.master,
            command=lambda: self.c.download_video(
                self.entry_widget, self.listbox_widget
            ),
            text="Submit",
        )

        self.progressbar_widget = CTkProgressBar(self.master)
        self.remove_widget = CTkButton(
            self.master,
            command=lambda: self.c.progress_the_bar(),
            text="Test progressbar",
        )

        # File dialog method
        self.my_text_widget = CTkLabel(
            self.master, text_color="green", width=100, height=70, text="file dialog"
        )
        self.browsefile_widget = CTkButton(
            self.master,
            width=10,
            height=10,
            command= self.c.open_downloads_path,
            text="Browse file",
        )

        # Checkbox state
        self.is_checked = IntVar()
        self.checkbox_widget = CTkCheckBox(
            self.master,
            text="CTkCheckBox",
            command=lambda: self.c.checkbox_event(self.is_checked),
            variable=self.is_checked,
            onvalue=1,
            offvalue=0,
        )

    def layout_widgets(self):
        # Place widgets using Grid
        self.label_widget.grid(row=0, column=0, padx=10, pady=10, columnspan=3)
        self.progressbar_widget.grid(
            row=1, column=0, padx=30, pady=30, columnspan=2, sticky="ew"
        )
        self.entry_widget.grid(row=2, column=0, padx=10, pady=10, columnspan=3)
        self.checkbox_widget.grid(row=3, column=3, padx=10, pady=10, sticky="e")
        self.submit_widget.grid(row=3, column=0, padx=10, pady=10)
        self.remove_widget.grid(row=3, column=1, padx=10, pady=10)
        self.listbox_widget.grid(
            row=5, column=0, padx=20, pady=20, sticky="ew", columnspan=2
        )
        self.browsefile_widget.grid(row=4, column=0, padx=10, pady=10)
        self.my_text_widget.grid(row=4, column=1, padx=10, pady=10, sticky="w")


class Main:
    def __init__(self):
        self.root = ctk.CTk()  # Create the main window
        self.root.title("Grid")
        self.root.geometry("700x570")

        # Initialize MyGUI with the main window
        self.gui = MyGUI(self.root)

    def run(self):
        self.root.mainloop()  # Start the main loop


if __name__ == "__main__":
    app = Main()
    app.run()  # This runs the app
