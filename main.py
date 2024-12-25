import customtkinter as ctk
from functions import get_url_from
import requests

# System settings
ctk.set_appearance_mode("dark")  # Modes: system (default), light dark
ctk.set_default_color_theme("dark-blue")  # Themes: blue (default), dark


class App(ctk.CTk):
    # Layout of the GUI will be written in the init itself
    def __init__(self):
        super().__init__()  # Call the parent class's constructor
        self.title(
            "Youtube to mp3 converter"
        )  # Use self to refer to the current instance
        # Dimensions of the window will be 200x200
        self.geometry("700x450")
        # Adding Ui Elements
        self.my_font = ctk.CTkFont(family="Helvetica", size=17)

        # This is the main label
        self.my_label = ctk.CTkLabel(
            master=self,
            text="Enter a Youtube URL: ",
            text_color="white",
            font=self.my_font,
        )
        self.my_label.pack(pady=40, padx=30)

        # # This is our Entry Widget where we add the URL
        self.entry = ctk.CTkEntry(
            master=self,  # Change app to self,
            placeholder_text="link",
            font=self.my_font,
            width=450,
            height=30,
            border_width=2,
            corner_radius=5,
        )
        self.entry.pack(pady=35, padx=35)

        # This is the button Widget to handle an event
        self.MyButton = ctk.CTkButton(
            master=self,  # Change app to self
            text="Convert to mp3",
            font=self.my_font,
            width=40,
            height=20,
            command=lambda: get_url_from(self.entry),  # Pass the entry widget
        )
        self.MyButton.pack(pady=25, padx=25)

        # A button to clear the entry widget
        self.clear_button = ctk.CTkButton(master=self, text="clear")
        self.clear_button.pack(pady=20, padx=20)
        self.clear_button.configure(command=lambda: (self.entry.delete(0, ctk.END)))


if __name__ == "__main__":
    app = App()
    # This runs the app
    app.mainloop()
