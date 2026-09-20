Yes — the two new projects are **📀 DVD Bouncing Logo** and **📅 Custom Calendar**. I’ve added them throughout the README: project structure, overview, and run commands. I’ve also added `bext` and `timedelta` to the relevant tech/library sections.

# 🧠 Python Simple Projects Collection

A collection of beginner-to-intermediate Python projects focused on strengthening core programming skills through hands-on implementation.

Each project explores a different programming concept—from simple command-line games to GUI applications and simulations—while emphasizing clean code, modular design, and problem-solving.

This repository focuses on:

* Problem-solving

* Algorithmic thinking

* Event-driven programming

* File handling and data persistence

* Simulations and probability

* Writing modular, maintainable code

* Incremental learning through practical projects

---

# 📂 Project Structure

```text
PYTHON-SIMPLE-PROJECTS/

│
├── number_guessing_game/
│   ├── main.py
│   └── README.md
│
├── bagels/
│   ├── main.py
│   └── README.md
│
├── birthday_paradox/
│   ├── main.py
│   └── README.md
│
├── rock_paper_scissors/
│   ├── main.py
│   └── README.md
│
├── to_do_list/
│   ├── to_do_list.py
│   ├── tasks.json
│   └── README.md
│
├── caesar_cipher/
│   ├── main.py
│   └── README.md
│
├── bitmap_message/
│   ├── main.py
│   └── README.md
│
├── blackjack/
│   ├── main.py
│   └── README.md
│
├── dvd_bouncing_logo/
│   ├── main.py
│   └── README.md
│
├── custom_calendar/
│   ├── main.py
│   └── README.md
│
├── README.md
└── .gitignore
```

---

# 🚀 Projects Overview

## 🎯 Number Guessing Game

A GUI-based game where the player guesses a randomly generated number within a limited number of attempts.

**Concepts Practiced**

* State management

* Event-driven programming

* Input validation

* Random number generation

* UI updates

* Game lifecycle handling

---

## 🥯 Bagels

A command-line implementation of the classic **Bagels** deduction game.

The computer generates a secret **3-digit number with unique digits**, and the player must guess it using the clues:

* **Fermi** – Correct digit in the correct position

* **Pico** – Correct digit in the wrong position

* **Bagels** – No correct digits

**Concepts Practiced**

* Game logic

* Random number generation

* Lists and strings

* Input validation

* Functions

* Conditional statements

* Loop control

* Problem-solving

---

## 🎂 Birthday Paradox

A simulation of the famous **Birthday Paradox**, demonstrating how surprisingly likely it is for two people in a group to share the same birthday.

The program generates random birthdays, checks for duplicate dates, and performs thousands of simulations to estimate the probability of a shared birthday.

**Concepts Practiced**

* Probability simulation

* Nested loops

* Date and time handling

* Random number generation

* Algorithmic thinking

* Performance through repeated simulations

* Functions and modular design

---

## 🪨✋✌️ Rock Paper Scissors

A GUI-based Rock Paper Scissors game where the player competes against the computer.

**Concepts Practiced**

* Event-driven programming

* Timers and delays

* Randomized gameplay

* State management

* UI control

---

## 📝 To-Do List (CLI)

A command-line task manager with persistent storage using JSON.

**Concepts Practiced**

* CRUD operations

* File handling

* JSON serialization

* Data persistence

* User interaction

---

## 🔐 Caesar Cipher

A text encryption and decryption tool based on the classical Caesar Cipher algorithm.

**Concepts Practiced**

* ASCII manipulation (`ord()` and `chr()`)

* Modular arithmetic

* String processing

* Loops

* Conditional logic

---

## 🖼️ Bitmap Message

A command-line program that displays a user-entered message within a predefined ASCII bitmap pattern.

**Concepts Practiced**

* Strings

* String indexing

* `splitlines()`

* `enumerate()`

* Loops

* Conditional statements

* String concatenation

* Modulo operator

* User input

---

## 🃏 Blackjack

A command-line implementation of the classic **Blackjack** card game. The player attempts to get as close to 21 as possible without going over while managing bets and playing against the dealer.

**Concepts Practiced**

* Functions

* Loops

* Lists and tuples

* Randomization with `random`

* User input

* Game logic

* Conditional statements

* String manipulation

* Unicode characters

* Modular program design

* Basic state and money management

---

## 📀 DVD Bouncing Logo

A terminal-based animation that recreates the classic **DVD logo bouncing around a screen**. Multiple logos move diagonally across the terminal, bouncing off the edges and changing to a random color whenever their direction changes. The program also keeps track of how many times a logo reaches a corner.

**Concepts Practiced**

* Dictionaries

* Lists and tuples

* State management

* Random number generation

* Terminal cursor positioning

* Terminal colors

* Simulation and animation

* External Python packages

* `KeyboardInterrupt` handling

---

## 📅 Custom Calendar

A command-line calendar generator that creates a formatted calendar for a user-selected year and month. The program calculates the correct starting weekday, arranges the dates into weekly rows, and displays holidays and custom events underneath their corresponding dates. I also added a few personal dates, making this project a little more than just a basic calendar generator.

**Concepts Practiced**

* `datetime.date`

* `timedelta`

* Dictionaries

* Tuples

* String formatting

* Date calculations

* Loops

* Input validation

* Exception handling

* Structured terminal output

---

# 🛠️ Tech Stack

* Python 3

* CustomTkinter (GUI projects)

* `bext` (Terminal animation)

* JSON (Data persistence)

### Standard Library Modules

* `random`

* `datetime`

* `timedelta`

* `json`

* `os`

* `pathlib`

* `sys`

* `time`

---

# ▶️ Getting Started

## 1. Clone the repository

```bash
git clone https://github.com/your-username/python-simple-projects.git

cd python-simple-projects
```

---

## 2. Install dependencies

Only required for projects that use external packages.

For GUI projects:

```bash
pip install customtkinter
```

For the DVD Bouncing Logo:

```bash
pip install bext
```

---

## 3. Run a project

### Number Guessing Game

```bash
python number_guessing_game/main.py
```

### Bagels

```bash
python bagels/main.py
```

### Birthday Paradox

```bash
python birthday_paradox/main.py
```

### Rock Paper Scissors

```bash
python rock_paper_scissors/main.py
```

### To-Do List

```bash
python to_do_list/to_do_list.py
```

### Caesar Cipher

```bash
python caesar_cipher/main.py
```

### Bitmap Message

```bash
python bitmap_message/main.py
```

### Blackjack

```bash
python blackjack/main.py
```

### DVD Bouncing Logo

```bash
python dvd_bouncing_logo/main.py
```

### Custom Calendar

```bash
python custom_calendar/main.py
```

---

# 🎯 Learning Goals

This repository is designed to strengthen:

* Python fundamentals

* Algorithmic thinking

* Problem-solving skills

* Program flow and state management

* File handling and persistence

* Code organization

* Writing reusable functions

* Building complete small-scale applications

---

# 🧠 Skills Demonstrated

Across these projects, you'll encounter:

* Functions

* Loops

* Conditional statements

* Lists, dictionaries, tuples, and strings

* Random number generation

* Date and time manipulation

* JSON handling

* File I/O

* Event-driven programming

* GUI development with CustomTkinter

* Terminal manipulation

* Simulation and animation

* Modular code organization

* Simulation-based programming

---

# 💡 Repository Philosophy

This repository represents the transition from writing simple scripts to developing complete, well-structured applications.

Each project focuses on a different aspect of software development:

* 🎮 Interactive game logic

* 🖥️ GUI application development

* 📂 Data persistence

* 🔐 Classical algorithms

* 🎲 Probability simulations

* 🖼️ Terminal graphics and animation

* 📅 Date and time manipulation

* 🧩 Problem decomposition

* 🏗️ Code organization and modularity

As new projects are completed, this repository will continue to grow into a comprehensive collection of Python applications that document my learning journey.

---

# 📚 Learning Resources

Many of these projects are inspired by excellent programming books and resources, including:

* *The Big Book of Small Python Projects* by Al Sweigart

They are implemented independently as part of my learning process.

---

# 📜 License

This project is licensed under the **MIT License**.

Feel free to use, modify, and learn from these projects.
