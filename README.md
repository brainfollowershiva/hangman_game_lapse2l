# 🎮 Hangman Game

> A classic word-guessing game built with Python | Strategic gameplay | Interactive CLI

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)]()

---

## 📋 Overview

**Hangman** is a strategic word-guessing game implementation in Python. Players attempt to guess a hidden word by suggesting letters within a limited number of attempts. Perfect for understanding game logic, user input handling, and state management.

### ✨ Features

- 🎯 **Dynamic Word Selection** - Random words from an extensive dictionary
- 🔤 **Smart Letter Tracking** - Manage guessed letters and remaining attempts
- 📊 **Game Statistics** - Track wins, losses, and success rate
- 🎨 **Clean CLI Interface** - User-friendly terminal-based gameplay
- ⚡ **Real-time Feedback** - Instant visual feedback on guesses
- 🔄 **Replay Functionality** - Play multiple rounds without restarting

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- No external dependencies

### Installation

```bash
# Clone repository
git clone https://github.com/brainfollowershiva/hangman_game_lapse2l.git
cd hangman_game_lapse2l

# Run the game
python hangman.py
```

### How to Play

1. **Start the game** - Run the Python script
2. **Guess letters** - Enter one letter per turn
3. **Win condition** - Guess all letters before running out of attempts
4. **Lose condition** - Run out of attempts before revealing the word
5. **Play again** - Choose to play another round

```
Word: _ _ _ _ _ _
Guesses left: 6
Guessed letters: []
Enter your guess: E

Word: _ _ _ _ _ E
Guesses left: 6
Guessed letters: [E]
```

---

## 🛠️ Technical Details

### Architecture

```
hangman_game_lapse2l/
├── hangman.py          # Main game logic
├── words.txt           # Word dictionary
├── README.md           # Documentation
└── LICENSE             # MIT License
```

### Core Components

| Component | Purpose |
|-----------|----------|
| **Word Manager** | Selects and manages hidden words |
| **Game State** | Tracks guesses, attempts, and progress |
| **Input Validator** | Validates player input and handles errors |
| **Display Logic** | Renders game state and user interface |

### Algorithm Explanation

1. **Initialization** - Load word list and select random word
2. **Game Loop** - Repeatedly get user input until win/lose condition
3. **Letter Checking** - Reveal correct letters or decrement attempts
4. **Win/Lose Detection** - Check if all letters revealed or attempts exhausted
5. **Replay Option** - Offer to play another round

---

## 📊 Game Statistics

Track your performance:
- Total games played
- Games won vs. games lost
- Average guesses per game
- Win/loss ratio

---

## 🎓 Learning Outcomes

Building this project teaches:
- ✅ Python fundamentals (loops, conditionals, functions)
- ✅ String manipulation and list operations
- ✅ Game state management
- ✅ User input validation and error handling
- ✅ Basic algorithms and logic design
- ✅ File I/O operations

---

## 🔄 Future Enhancements

- [ ] Difficulty levels (Easy/Medium/Hard)
- [ ] Category-based word selection
- [ ] Hint system
- [ ] Leaderboard tracking
- [ ] GUI version with Tkinter
- [ ] Multiplayer mode
- [ ] Custom word dictionary

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs and issues
- Suggest improvements
- Submit pull requests
- Improve documentation

---

## 📝 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Shiva Ram**
- 🎓 B.Tech AIML Student
- 💻 Python Developer
- 🔗 [GitHub](https://github.com/brainfollowershiva)
- 📧 [Email](mailto:siv.dev022@gmail.com)

---

<div align="center">

**[⬆ Back to Top](#-hangman-game)**

Built with ❤️ by Shiva Ram

</div>