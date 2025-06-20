# 🎮 Hangman Game

A GUI-based **Hangman Game** developed in Python using **Tkinter** for the interface and **Pygame** for sound effects. The game includes a clean graphical interface, background music, category-based word selection, and fun sound feedback for user interaction.

---

## 🧩 Features

- 🖼️ User-friendly graphical interface
- 🔊 Background music and sound effects
- 📚 Category selection (Animal, Fruit, Name, Vegetable)
- ✅ Play and Exit buttons with hover animation
- 📄 Word data loaded from `.txt` files
- 🎯 Game logic handled in a separate module (`hangman.py`)

---

## 🛠 Requirements

- Python 3.10+ (works on 3.13 too)
- Libraries:
  - `pygame`
  - `Pillow` (for images)
  - `tkinter` (comes with Python)

Install required libraries:

```bash
pip install pygame pillow
```

---

## 🚀 How to Run

1. Download or clone this repository.
2. Ensure all game assets are in the same folder:
   - `.wav` files for sound
   - `.txt` files for words
   - `.jpg` for background
3. Run the game from the terminal or your IDE:

```bash
python "Main menu.py"
```

---

## 📁 File Structure

| File            | Description                            |
|-----------------|----------------------------------------|
| `Main menu.py`  | Main menu screen with category buttons |
| `hangman.py`    | Core game logic and word guessing      |
| `music.wav`     | Background music                       |
| `click.wav`     | Button click sound                     |
| `photo.jpg`     | Background image                       |
| `fruit.txt`     | Fruit words                            |
| `animal.txt`    | Animal words                           |
| `name.txt`      | Name list                              |
| `vegetable.txt` | Vegetable words                        |

---

## 📦 Optional: Build into `.exe`

To package the game into a standalone `.exe` using `pyinstaller`:

```bash
pyinstaller --onefile --windowed ^
--add-data "music.wav;." ^
--add-data "click.wav;." ^
--add-data "photo.jpg;." ^
--add-data "fruit.txt;." ^
--add-data "animal.txt;." ^
--add-data "name.txt;." ^
--add-data "vegetable.txt;." ^
"Main menu.py"
```

After building, go to the `dist/` folder and run `Main menu.exe`.

---


## 👨‍💻 Developer

**Usman Ali**  
🎓 IT Student | 🇵🇰 Pakistan  
💻 Passionate about programming and game development

---

## 📃 License

This project is currently for learning purposes. You may freely use and modify it.

---

> ⭐ *If you like this project, give it a star on GitHub!*

PRO TIP:  
DOWNLOAD full folder of game and run "main menu.py" and game will run 
ENJOY IT!!!!!!!!!!!!!!!!!!!!!!!!!!!!
