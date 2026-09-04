# 🃏 Blackjack Game — Python

A simple **command-line Blackjack game built with Python**. The game uses a shuffled deck, allows the player to **Hit, Stand, or Double Down**, and keeps track of the player's money throughout multiple rounds.This project was created as part of my practice with The Big Book of Small Python Projects by Al Sweigart.

## 🎮 Features

* 🃏 Standard 52-card deck
* 🔀 Randomly shuffled cards
* 💰 Betting system starting with **$5000**
* 👤 Player and dealer hands
* ❤️ Card suits displayed using Unicode symbols
* 🎯 Hit and Stand actions
* 💵 Double Down option
* 🧮 Automatic hand-value calculation
* 🤖 Dealer automatically draws until reaching at least 17
* 💸 Win, lose, and tie handling
* 🃏 Hidden dealer card during the player's turn
* 🚪 Option to quit the game

## 📜 Rules

The game follows these basic Blackjack rules:

* Try to get as close to **21** as possible without going over.
* Kings, Queens, and Jacks are worth **10 points**.
* Aces are worth **1 or 11 points**.
* Cards from 2 to 10 are worth their face value.
* **Hit** → Draw another card.
* **Stand** → Stop taking cards.
* **Double Down** → Double the bet and draw exactly one more card.
* If the player and dealer have the same value, the bet is returned.
* The dealer keeps drawing while their hand is **16 or below**.

## 🕹️ How to Play

### 1. Start the game

Run the Python file:

```bash
python blackjack.py
```

The game starts with:

```text
Money: $5000
Enter the bet amount:
```

Enter the amount you want to bet.

### 2. Choose an action

During your turn, you can choose:

```text
Valid Moves:
(H)it, (S)tand, (D)oubleDown
```

* `H` — Draw another card
* `S` — End your turn
* `D` — Double your bet and draw one more card

### 3. Compare hands

After the player finishes their turn, the dealer reveals their hidden card and draws cards until their hand reaches at least 17.

The game then compares the two hands and determines the result.

## 💰 Betting System

The game begins with:

```text
$5000
```

If the player wins, the bet is added to their money.

If the player loses, the bet is deducted.

If the game ends in a tie, the player's money remains unchanged.

## 🏗️ Program Structure

The project is divided into several functions:

| Function         | Purpose                                |
| ---------------- | -------------------------------------- |
| `main()`         | Controls the main game loop            |
| `AskBet()`       | Gets and validates the player's bet    |
| `GetDeck()`      | Creates and shuffles the deck          |
| `getHands()`     | Displays the dealer and player's hands |
| `displayHands()` | Creates the visual card representation |
| `getHandValue()` | Calculates the value of a hand         |
| `getMove()`      | Gets the player's action               |

## 🃏 Card Representation

Cards are stored as tuples containing their suit and value.

For example:

```python
("♥", 10)
("♠", "K")
("♦", "A")
```

The four suits are represented using Unicode characters:

```python
HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
```

## 🧠 Technologies Used

* **Python**
* `random` — used to shuffle the deck
* `sys` — used to exit the program

## 📚 What This Project Practices

This project demonstrates several important Python concepts:

* Functions
* Lists
* Tuples
* Loops
* Conditional statements
* User input
* String formatting
* Randomization
* List manipulation
* Basic game logic
* Function parameters and return values
* Docstrings

## 🚀 Future Improvements

Possible improvements for future versions:

* Add proper Blackjack rules for Aces
* Add Blackjack detection
* Improve Double Down validation
* Add multiple players
* Add betting statistics
* Add chips instead of a simple money value
* Add a replay/menu system
* Improve input validation
* Add unit tests
* Create a graphical version using **Pygame**

## 👨‍💻 Project

This project was created as a Python practice project while learning programming and game development concepts.
