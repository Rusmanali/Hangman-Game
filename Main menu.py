import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pygame
import sys
import os
from hangman import game_window

# Path helper function
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(base_path, relative_path)

# Initialize pygame mixer
pygame.mixer.init()

def play_music():
    try:
        music_path = resource_path("music.wav")
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.play(-1)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load music: {e}")

def on_enter(e):
    e.widget.config(bg="#4ccf9d", fg="white")

def on_leave(e):
    e.widget.config(bg="#003d26", fg="white")

def open_category_window():
    category_window = tk.Toplevel(root)
    category_window.title("Select Category")
    category_window.geometry("500x400")
    
    try:
        bg_path = resource_path("photo.jpg")
        bg_image = Image.open(bg_path).resize((500, 400), Image.LANCZOS)
        bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = tk.Label(category_window, image=bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        category_window.bg_photo = bg_photo
    except Exception as e:
        messagebox.showerror("Error", f"Could not load background: {e}")
        bg_label = tk.Label(category_window, bg="black")
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    category_label = tk.Label(
        category_window, text="Select a Category", font=("Algerian", 18, "bold"),
        bg="black", fg="#b2f00a", padx=10, pady=5
    )
    category_label.pack(pady=20)

    def start_game(category):
        pygame.mixer.music.stop()
        category_window.destroy()
        root.destroy()
        game_window(category)

    button_style = {
        "font": ("Arial", 14), "width": 15,
        "bg": "#003d26", "fg": "white", "bd": 0, "relief": "flat"
    }

    categories = ["Animal", "Name", "Fruit", "Vegetable"]
    for category in categories:
        btn = tk.Button(category_window, text=category,
                       command=lambda c=category: start_game(c), **button_style)
        btn.pack(pady=5)
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)

def exit_game():
    pygame.mixer.music.stop()
    root.destroy()

root = tk.Tk()
root.title("Hangman - Main Menu")
root.geometry("500x400")

try:
    bg_path = resource_path("photo.jpg")
    bg_image = Image.open(bg_path).resize((500, 400), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    root.bg_photo = bg_photo
except Exception as e:
    messagebox.showerror("Error", f"Could not load background: {e}")
    bg_label = tk.Label(root, bg="black")
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

play_music()

heading_label = tk.Label(
    root, text="HANG MAN", font=("Algerian", 30, "bold"),
    fg="#b2f00a", bg="black", padx=10, pady=5
)
heading_label.place(x=135, y=50)

btn_play = tk.Button(
    root, text="Play", font=("Arial", 14), command=open_category_window,
    width=15, bg="#003d26", fg="white", bd=0, relief="flat"
)
btn_play.place(x=170, y=150)
btn_play.bind("<Enter>", on_enter)
btn_play.bind("<Leave>", on_leave)

btn_exit = tk.Button(
    root, text="Exit", font=("Arial", 14), command=exit_game,
    width=15, bg="#003d26", fg="white", bd=0, relief="flat"
)
btn_exit.place(x=170, y=200)
btn_exit.bind("<Enter>", on_enter)
btn_exit.bind("<Leave>", on_leave)

root.mainloop()