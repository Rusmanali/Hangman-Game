import random
import pygame
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

pygame.mixer.init()

try:
    click_sound = pygame.mixer.Sound("click.wav")
    win_sound = pygame.mixer.Sound("win.wav")
    lose_sound = pygame.mixer.Sound("lose.wav")
except Exception as e:
    print("Could not load sound files:", e)

score = 0
run = True

def load_words(filename):
    try:
        with open(filename, 'r') as file:
            return [word.strip().lower() for word in file.readlines() if word.strip()]
    except Exception as e:
        print(f"Could not load {filename}:", e)
        return []

categories = {
    "Animal": load_words("animal.txt"),
    "Name": load_words("name.txt"),
    "Fruit": load_words("fruit.txt"),
    "Vegetable": load_words("vegetable.txt")
}

def game_window(category):
    global run, score
    game_root = Tk()
    game_root.geometry('905x700')
    game_root.title('HANGMAN')
    game_root.config(bg='#a3e68e')

    count = 0
    win_count = 0
    selected_word = random.choice(categories[category])

    dashes = []
    for i in range(len(selected_word)):
        lbl = Label(game_root, text="_", bg="#a3e68e", font=("arial", 40))
        lbl.place(x=250 + (i * 60), y=450)
        dashes.append(lbl)

    letter_images = {}
    for let in 'abcdefghijklmnopqrstuvwxyz':
        try:
            letter_images[let] = PhotoImage(file=f"{let}.png")
        except:
            letter_images[let] = PhotoImage()

    hangman_images = []
    for i in range(1, 8):
        try:
            hangman_images.append(PhotoImage(file=f"h{i}.png"))
        except:
            hangman_images.append(PhotoImage())

    hangman_label = Label(game_root, bg="#a3e68e", image=hangman_images[0])
    hangman_label.place(x=300, y=-50)

    hearts = []
    try:
        heart_full = ImageTk.PhotoImage(Image.open("heart1.png").resize((20, 20), Image.LANCZOS))
    except:
        heart_full = PhotoImage()
    try:
        heart_empty = ImageTk.PhotoImage(Image.open("heart2.png").resize((20, 20), Image.LANCZOS))
    except:
        heart_empty = PhotoImage()

    for i in range(6):
        heart_label = Label(game_root, image=heart_full, bg="#a3e68e")
        heart_label.place(x=20 + i * 30, y=60)
        hearts.append(heart_label)

    Label(game_root, text=f"Category: {category}", bg="#a3e68e", font=("arial", 20)).place(x=20, y=100)

    def close():
        global run
        if messagebox.askyesno('ALERT', 'DO YOU WANT TO EXIT THE GAME?'):
            run = False
            game_root.destroy()

    try:
        ex_img = PhotoImage(file='exit.png')
    except:
        ex_img = PhotoImage()

    Button(game_root, bd=0, command=close, bg="#a3e68e", activebackground="#a3e68e", image=ex_img).place(x=770, y=10)
    Label(game_root, text=f'SCORE: {score}', bg="#a3e68e", font=("arial", 25)).place(x=10, y=10)

    def check(letter, button):
        nonlocal count, win_count
        try:
            click_sound.play()
        except:
            pass
        button.destroy()
        if letter in selected_word:
            for i, char in enumerate(selected_word):
                if char == letter:
                    win_count += 1
                    dashes[i].config(text=letter.upper())
            if win_count == len(selected_word):
                try:
                    win_sound.play()
                except:
                    pass
                global score
                score += 1
                if messagebox.askyesno('GAME OVER', 'YOU WON!\nWANT TO PLAY AGAIN?'):
                    game_root.destroy()
                    game_window(category)
                else:
                    run = False
                    game_root.destroy()
        else:
            count += 1
            if count > 0:
                hearts[6 - count].config(image=heart_empty)
            if count < 7:
                hangman_label.config(image=hangman_images[count])
            if count == 6:
                try:
                    lose_sound.play()
                except:
                    pass
                messagebox.showinfo("GAME OVER", f"YOU LOST! The correct word was: {selected_word.upper()}")
                if messagebox.askyesno('GAME OVER', 'WANT TO PLAY AGAIN?'):
                    game_root.destroy()
                    game_window(category)
                else:
                    run = False
                    game_root.destroy()

    button_positions = [(chr(97 + i), (i % 13) * 70, 550 if i < 13 else 600) for i in range(26)]
    for letter, x, y in button_positions:
        btn = Button(game_root, bd=0, bg="#a3e68e", activebackground="#a3e68e", image=letter_images[letter])
        btn.config(command=lambda l=letter, b=btn: check(l, b))
        btn.place(x=x, y=y)

    game_root.mainloop()

# ✅ Corrected main block for standalone testing
if __name__ == "__main__":
    game_window("Animal")
