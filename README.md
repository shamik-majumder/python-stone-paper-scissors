# python-stone-paper-scissors
A simple, interactive, command-line implementation of the classic Stone, Paper, Scissors (Rock, Paper, Scissors) game written in Python.
# Stone, Paper, Scissors Game

A lightweight, console-based implementation of the classic **Stone, Paper, Scissors** (Rock, Paper, Scissors) game built using Python. 

## Features
* **Randomised Opponent:** The computer uses Python's standard `random` library to select its move unpredictably.
* **Input Validation:** Built-in validation filters out incorrect keystrokes, ensuring only valid game inputs are processed.
* **Case Insensitivity:** Automatically normalises user entries so typing capital letters won't crash your game loop.
* **Modular Code:** Uses a dedicated game logic function (`determine_winner`) making it highly reusable and easy to extend.

## How to Play
The game follows traditional rules:
* 🪨 **Stone ('s')** beats Scissor ('c')
* 📄 **Paper ('p')** beats Stone ('s')
* ✂️ **Scissor ('c')** beats Paper ('p')

## Prerequisites
* Python 3.x installed on your computer.

## Setup & Running the Game
1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd python-stone-paper-scissors
   ```

2. **Run the script:**
   ```bash
   python main.py
   ```

## File Structure
* `main.py` - Contains the logic functions and the active command-line game sequence.
