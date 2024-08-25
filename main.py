import tkinter as tk
from tkinter import filedialog
import pygame
from datetime import datetime
from PIL import Image, ImageTk

pygame.mixer.init()

def load_file():
    file_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
    if file_path:
        playlist_box.insert(tk.END, file_path)
        play_file(file_path)
        file_label.config(text=file_path.split('\\')[-1])

def play_playlist_file():
    selected = playlist_box.curselection()
    if selected:
        file_path = playlist_box.get(selected[0])
        play_file(file_path)

def play_file(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    file_label.config(text=file_path.split('\\')[-1])

def pause_music():
    pygame.mixer.music.pause()

def unpause_music():
    pygame.mixer.music.unpause()

def stop_music():
    pygame.mixer.music.stop()

def play_time_based_sound():
    current_hour = datetime.now().hour
    if 6 <= current_hour < 12:
        sound_file = 'D:\\uta_chan\\VOICE\\おはようございます.wav'
    elif 12 <= current_hour < 18:
        sound_file = 'D:\\uta_chan\\VOICE\\こんにちは.wav'
    elif 18 <= current_hour < 22:
        sound_file = 'D:\\uta_chan\\VOICE\\こんばんは.wav'
    else:
        sound_file = 'D:\\uta_chan\\VOICE\\おやすみなさい.wav'

    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()

def play_closing_sound():
    closing_file = 'D:\\uta_chan\\VOICE\\ご利用いただき.wav'
    pygame.mixer.music.load(closing_file)
    pygame.mixer.music.play()
    root.after(int(pygame.mixer.Sound(closing_file).get_length() * 1000), root.destroy)

def clear_playlist():
    playlist_box.delete(0, tk.END)

root = tk.Tk()
root.title("Mini MP3 Player")
root.geometry('600x400')
root.resizable(False, False)

icon_image = Image.open('D:\\uta_chan\\IMG\\icon.jpg')
icon_photo = ImageTk.PhotoImage(icon_image)
root.iconphoto(False, icon_photo)

button_frame = tk.Frame(root)
button_frame.place(relx=0.1, rely=0.5, anchor=tk.CENTER)

button_width = 10
button_height = 2

load_button = tk.Button(button_frame, text="Load & Play", command=load_file, width=button_width, height=button_height)
play_button = tk.Button(button_frame, text="Play", command=play_playlist_file, width=button_width, height=button_height)
pause_button = tk.Button(button_frame, text="Pause", command=pause_music, width=button_width, height=button_height)
unpause_button = tk.Button(button_frame, text="Unpause", command=unpause_music, width=button_width, height=button_height)
stop_button = tk.Button(button_frame, text="Stop", command=stop_music, width=button_width, height=button_height)
clear_playlist_button = tk.Button(button_frame, text="Clear Playlist", command=clear_playlist, width=button_width, height=button_height)

load_button.pack(pady=5)
play_button.pack(pady=5)
pause_button.pack(pady=5)
unpause_button.pack(pady=5)
stop_button.pack(pady=5)
clear_playlist_button.pack(pady=5)

info_frame = tk.Frame(root, padx=10, pady=10)
info_frame.place(relx=0.75, rely=0.5, anchor=tk.CENTER)

playlist_box = tk.Listbox(info_frame, width=40, height=10)
playlist_box.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

file_label = tk.Label(info_frame, text="No file loaded", wraplength=200)
file_label.pack(side=tk.BOTTOM, pady=10)

play_time_based_sound()

root.protocol("WM_DELETE_WINDOW", play_closing_sound)

root.mainloop()
