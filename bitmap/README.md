# 🖼️ Bitmap Message

A simple **command-line bitmap message generator** built in Python. This project was created as part of my practice with **The Big Book of Small Python Projects** by **Al Sweigart**.

## 💡 About the Project

This program takes a message entered by the user and displays it inside a predefined **ASCII bitmap pattern**.

The bitmap contains characters such as `*` and spaces. The program replaces the non-space characters with characters from the user's message, creating a repeating text pattern.

For example, if the user enters a message such as:

```text
HELLO
```

the letters are repeatedly placed across the bitmap to create the final design.

## ✨ Features

* 🖼️ Predefined ASCII bitmap pattern
* ⌨️ Accepts a message from the user
* 🔄 Repeats the message across the bitmap
* 🧩 Preserves spaces in the original bitmap
* 🚫 Prevents an empty/space-only message
* 🖥️ Displays the generated bitmap directly in the terminal

## 🛠️ Concepts Practiced

This project helped me practice:

* Strings
* String slicing and indexing
* `splitlines()`
* `for` loops
* `enumerate()`
* Conditional statements
* User input
* String concatenation
* Modulo operator `%`
* Working with ASCII-style patterns

## 🔍 How It Works

The program:

1. Stores the bitmap pattern in a multiline string.
2. Asks the user to enter a message.
3. Goes through each line of the bitmap.
4. Checks every character in the line.
5. Keeps spaces unchanged.
6. Replaces every non-space character with a character from the user's message.
7. Uses `% len(msg)` so the message repeats when the bitmap is longer than the message.
8. Prints the resulting bitmap.

## ▶️ How to Run

Make sure Python is installed, then run:

```bash
python bitmap_message.py
```

Enter a message when prompted:

```text
enter a message: HELLO
```

The program will generate the bitmap message in the terminal.

## 📚 Source

This project is based on a project from:

**The Big Book of Small Python Projects**
by **Al Sweigart**

It was used as a learning exercise to practice Python strings, loops, indexing, and basic text manipulation.
