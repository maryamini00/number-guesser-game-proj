# 🎲 Number Guesser Game

A modular and interactive CLI-based game built with Python.

## 🌟 Overview
This is not just a simple "Guess the Number" game. It is a project focused on practicing **Clean Code** and **Modular Programming** principles. The game challenges the user to guess a random number between 1 and 100, providing real-time hints and managing a scoring system.

What makes this project special is the **personality** of the game—it interacts with the user in a friendly, sometimes playful way, making the debugging and logic-testing process much more engaging.

## 🛠️ Technical Highlights
Instead of a monolithic script, I implemented a decoupled architecture:
- **`src/main.py`**: The central orchestrator of the game loop.
- **`src/game_logic/`**: Handles the core mechanics (score calculation, number selection, and hint logic).
- **`src/utils/`**: Manages user interaction, including input validation and UI/UX (printing titles and formatted outputs).

### Key Features:
- **Smart Hints:** The game doesn't just say "wrong"; it tells you if you need to go higher or lower, and even detects if you are repeating the same mistake.
- **Robust Input Validation:** Ensures the user enters valid integers and handles "exit" commands gracefully.
- **Dynamic Scoring:** A system where you lose points for wrong guesses and gain points for perfect matches.

## 📂 Project Structure
```text
src/
├── main.py
├── game_logic/
│   ├── hint_handling.py
│   ├── score_handling.py
│   └── selected_number.py
└── utils/
├── input_validator.py
└── titles_prints.py
```
## 🧠 Learning Outcomes
Through this project, I reinforced my understanding of:

Pythonic modularity and package structure.
Advanced control flow and input sanitization.
Logic separation for scalable software design.