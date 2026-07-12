# 🥯 Bagels - Number Guessing Game

A command-line implementation of the classic **Bagels** deduction game written in **Python**.

The computer generates a random **3-digit number with no repeated digits**, and your objective is to guess it within **10 attempts** using the clues provided after each guess.

---

## 📂 Project Structure

```
bagels/
│
├── main.py        # Main game logic
└── README.md      # Project documentation
```

---

## 🎮 How to Play

The computer secretly generates a **3-digit number** where every digit is unique.

After each guess, you receive one or more clues:

| Clue | Meaning |
|------|---------|
| **Fermi** | A digit is correct and in the correct position. |
| **Pico** | A digit is correct but in the wrong position. |
| **Bagels** | None of the digits are correct. |

The clues are sorted alphabetically, so they **do not indicate which digit they correspond to**.

You have **10 guesses** to find the secret number.

---

## 💻 Example Gameplay

```text
I am thinking of a 3-digit number. Try to guess what it is.

Here are some clues:

When I say:      That means:
Pico             One digit is correct but in the wrong position.
Fermi            One digit is correct and in the right position.
Bagels           No digit is correct.

I have thought up a number.
You have 10 guesses to get it.

Guess #1: 123
Bagels
Guesses left: 9

Guess #2: 582
Pico
Guesses left: 8

Guess #3: 528
Fermi Pico
Guesses left: 7

Guess #4: 548
Fermi Fermi Pico
Guesses left: 6

Guess #5: 584
Fermi Fermi Fermi

You got it!
Correct number is 584
```

---

## 🚀 Features

- 🎲 Random secret number generation
- 🔢 Three unique digits (no duplicates)
- 💡 Pico, Fermi, and Bagels clue system
- ✅ Input validation
- ⏳ 10-guess limit
- 📉 Remaining guesses displayed after each incorrect attempt
- 🔄 Replay option

---

## 🛠 Technologies Used

- Python 3
- Built-in `random` module

---

## 📚 Python Concepts Practiced

- Functions
- Loops (`for` and `while`)
- Conditional statements
- Lists
- Strings
- Input validation
- Random number generation
- List shuffling
- Game loop design

---

## ⚙️ Functions

### `guess_number(NUM_DIGITS)`
Generates a random secret number with unique digits.

### `clue_check(num, user_guess)`
Compares the player's guess with the secret number and returns the appropriate clues.

### `correct_answer_check(clues)`
Determines whether the player has guessed the secret number correctly.

### `main()`
Runs the complete game loop, including input validation, clue generation, guess tracking, and replay functionality.

---

## ▶️ Running the Game

Clone the repository:

```bash
git clone https://github.com/your-username/bagels-game.git
```

Navigate to the project folder:

```bash
cd bagels-game
```

Run the game:

```bash
python main.py
```

---

## 🚀 Future Improvements

- Prevent guesses with repeated digits.
- Support different difficulty levels (3, 4, or 5 digits).
- Add a scoring system.
- Store high scores.
- Add colored terminal output.
- Build a graphical version using Tkinter or Pygame.
- Write automated unit tests.

---

## 📖 Inspiration

This project is inspired by the **Bagels** game from **The Big Book of Small Python Projects** by **Al Sweigart**.

---

## 📄 License

This project is open-source and intended for educational and learning purposes.