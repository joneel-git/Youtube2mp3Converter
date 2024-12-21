import customtkinter
from functions import get_url_from
import requests

# System settings
customtkinter.set_appearance_mode("dark")  # Modes: system (default), light dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark

# Our app frame
app = customtkinter.CTk()
app.title("Youtube to mp3 converter")
app.geometry("700x450")

# Adding Ui Elements
my_font = customtkinter.CTkFont(family="Helvetica", size=17)

# This is the main label
my_label = customtkinter.CTkLabel(
    app, text="Enter a Youtube URL: ", text_color="white", font=my_font
)
my_label.pack(pady=50, padx=30)

# # This is our Entry Widget where we add the URL
entry = customtkinter.CTkEntry(
    master=app,
    placeholder_text="link",
    font=my_font,
    width=450,
    height=30,
    border_width=2,
    corner_radius=5,
)
entry.pack(padx=33, pady=33)


# This is the button Widget to handle an event
MyButton1 = customtkinter.CTkButton(
    app,
    text="Convert to mp3",
    font=my_font,
    width=40,
    height=20,
    command=lambda: get_url_from(entry) # Pass the entry widget
    )
MyButton1.pack(padx=20, pady=30)

# A button to clear the entry widget
clear_button = customtkinter.CTkButton(app, text="clear")
clear_button.pack(padx=33, pady=10)
clear_button.configure(command=lambda: (entry.delete(0, customtkinter.END)))


# download_label.configure(text="")
# Handle app closing
# Function to handle window closing
def on_closing():
    app.destroy()  # Close the application
    app.quit()  # Ensure the program exits completely


# Set the protocol for window closing
app.protocol("WM_DELETE_WINDOW", on_closing)

# Run App
app.mainloop()
