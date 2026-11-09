# ✊✋✌️ Stone, Paper, Scissors in Python

A clean, lightweight command-line implementation of the classic **Stone, Paper, Scissors** game built in Python. This project features robust input validation, randomized computer decision-making, and a modular function-based design for determining game outcomes.

---

## 🚀 Features

* **Modular Architecture:** Game rules and outcome calculations are neatly separated into dedicated functions (`determine_winner`).
* **Input Validation:** Safely handles invalid inputs and converts user keystrokes to lowercase automatically.
* **Randomized AI:** Utilizes Python's built-in `random` module to ensure unpredictable computer choices.
* **Beginner-Friendly Code:** Written with clear inline documentation, making it an excellent resource for learning fundamental Python concepts (functions, conditionals, and modules).

---

## 📋 Prerequisites

Make sure you have **Python 3.x** installed on your machine. You don't need to install any external libraries since this project uses Python's built-in standard library (`random`).

🎮 How to Run
Clone the repository:

Bash
git clone [https://github.com/YOUR_USERNAME/python-stone-paper-scissors.git](https://github.com/YOUR_USERNAME/python-stone-paper-scissors.git)
Navigate to the project directory:

Bash
cd python-stone-paper-scissors
Run the script:

Bash
python rps_game.py
🕹️ How to Play
When you run the script, you will be prompted to enter your choice using single-letter abbreviations:

Type s for Stone ✊

Type p for Paper ✋

Type c for Scissor ✌️

The program will instantly display your choice, the computer's randomized choice, and whether you won, lost, or tied!

🛠️ Code Snippet Overview
Here is how the game core evaluates the winner using concise conditional logic:

Python
def determine_winner(comp_choice, user_choice):
    if comp_choice == user_choice:
        return "Tie" 
    elif (user_choice == 's' and comp_choice == 'c') or \
         (user_choice == 'p' and comp_choice == 's') or \
         (user_choice == 'c' and comp_choice == 'p'):
        return "Win" 
    else:
        return "Lose"
📜 License
This project is open source and available under the MIT License.

