import tkinter as tk
from tkinter import messagebox, ttk
import subprocess
import re
import os
import threading

def is_playlist(url):
    return "playlist" in url

def run_download(command):
    try:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        for line in process.stdout:
            line = line.decode('utf-8')
            if "Downloading" in line:
                # Update the progress bar based on the output (you can customize this)
                progress_bar['value'] += 10  # Increment progress (adjust as needed)
                root.update_idletasks()  # Update the GUI

        process.wait()  # Wait for the process to complete
        messagebox.showinfo("Success", "Conversion completed successfully!")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def convert_to_mp3():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Input Error", "Please enter a YouTube URL.")
        return

    current_dir = os.path.dirname(os.path.abspath(__file__))
    yt_dlp_path = os.path.join(current_dir, 'yt-dlp.exe')

    if is_playlist(url):
        response = messagebox.askyesno("Playlist Detected", "This is a playlist. Do you want to download the entire playlist?")
        if response:
            command = f'"{yt_dlp_path}" -x --audio-format mp3 --output "%(title)s.%(ext)s" "{url}"'
        else:
            video_id = re.search(r'(?<=list=)[^&]+', url)
            if video_id:
                command = f'"{yt_dlp_path}" -f best -g "{url}"'
                video_url = subprocess.check_output(command, shell=True).decode('utf-8').strip()
                command = f'"{yt_dlp_path}" -x --audio-format mp3 --output "%(title)s.%(ext)s" "{video_url}"'
            else:
                messagebox.showerror("Error", "Could not extract video ID from the playlist URL.")
                return
    else:
        command = f'"{yt_dlp_path}" -x --audio-format mp3 --output "%(title)s.%(ext)s" "{url}"'

    threading.Thread(target=run_download, args=(command,)).start()

# Create the main window
root = tk.Tk()
root.title("YouTube to MP3 Converter")
root.geometry("600x300")  # Set the window size (width x height)

# Create and place the input field
url_label = tk.Label(root, text="Enter YouTube URL:", font=("Arial", 14))  # Larger font
url_label.pack(pady=10)

url_entry = tk.Entry(root, width=70, font=("Arial", 12))  # Larger font and wider entry
url_entry.pack(pady=5)

# Create and place the convert button
convert_button = tk.Button(root, text="Convert to MP3", command=convert_to_mp3, font=("Arial", 12), width=20)  # Larger font and button width
convert_button.pack(pady=20)

# Create and place the progress bar
progress_bar = ttk.Progressbar(root, length=400, mode='determinate')  # Make the progress bar longer
progress_bar.pack(pady=10)

# Run the application
root.mainloop()
