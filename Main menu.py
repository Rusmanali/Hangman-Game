import tkinter as tk
from PIL import Image, ImageTk
import pygame
import sys
import os
from hangman import game_window  # Import from hangman.py

# Path helper (for EXE compatibility)
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # Used when compiled to EXE
    except Exception:
        base_path = os.path.abspath(".")  # Used during development
    return os.path.join(base_path, relative_path)

# Initialize pygame mixer
pygame.mixer.init()

# Play background music
def play_music():
    try:
        pygame.mixer.music.load(resource_path("music.wav"))
        pygame.mixer.music.play(-1)
    except Exception as e:
        print("Could not load music file:", e)

# Button hover effects
def on_enter(e):
    e.widget.config(bg="#4ccf9d", fg="white")

def on_leave(e):
    e.widget.config(bg="#003d26", fg="white")

# Open category selection window
def open_category_window():
    category_window = tk.Toplevel(root)
    category_window.title("Select Category")
    category_window.geometry("500x400")

    # Background image
    try:
        bg_image = Image.open(resource_path("photo.jpg")).resize((500, 400), Image.LANCZOS)
        bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = tk.Label(category_window, image=bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        category_window.bg_photo = bg_photo
    except Exception as e:
        print("Could not load background image:", e)
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

# Exit the game
def exit_game():
    pygame.mixer.music.stop()
    root.destroy()

# Main Menu Window
root = tk.Tk()
root.title("Hangman - Main Menu")
root.geometry("500x400")

# Background image
try:
    bg_image = Image.open(resource_path("photo.jpg")).resize((500, 400), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    root.bg_photo = bg_photo
except Exception as e:
    print("Could not load background image:", e)
    bg_label = tk.Label(root, bg="black")
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Play music
play_music()

# Heading
heading_label = tk.Label(
    root, text="HANG MAN", font=("Algerian", 30, "bold"),
    fg="#b2f00a", bg="black", padx=10, pady=5
)
heading_label.place(x=135, y=50)

# Play button
btn_play = tk.Button(
    root, text="Play", font=("Arial", 14), command=open_category_window,
    width=15, bg="#003d26", fg="white", bd=0, relief="flat"
)
btn_play.place(x=170, y=150)
btn_play.bind("<Enter>", on_enter)
btn_play.bind("<Leave>", on_leave)

# Exit button
btn_exit = tk.Button(
    root, text="Exit", font=("Arial", 14), command=exit_game,
    width=15, bg="#003d26", fg="white", bd=0, relief="flat"
)
btn_exit.place(x=170, y=200)
btn_exit.bind("<Enter>", on_enter)
btn_exit.bind("<Leave>", on_leave)

root.mainloop()
