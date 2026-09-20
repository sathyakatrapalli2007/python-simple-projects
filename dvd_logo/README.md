Yep — this is the **DVD Bouncing Logo** project. Since it’s another project from *The Big Book of Small Python Projects*, I’d keep the README personal but still technical enough for your repository.

# 📀 DVD Bouncing Logo

A small terminal animation that recreates the classic **DVD logo bouncing around a screen**, changing direction whenever it hits an edge and changing color whenever it bounces. This project was another fun exercise from *The Big Book of Small Python Projects* by Al Sweigart, and it gave me a chance to play around with terminal graphics, movement, and simple simulation logic.

## 🎮 About the Project

The program creates multiple `DVD` logos that move diagonally around the terminal window. Each logo keeps track of its position, direction, and color, and the program continuously updates these values to create the animation.

Whenever a logo reaches the edge of the terminal, its direction is changed so that it appears to bounce off the wall. If it reaches a corner, the program also keeps track of the number of corner touches. The logo changes to a random color whenever its direction changes, making the animation a little more colorful and chaotic.

## ✨ Features

* 📀 Multiple bouncing DVD logos
* 🎨 Random colors
* ↗️ Diagonal movement
* 🧱 Automatic bouncing off terminal edges
* 🔲 Corner-bounce counter
* 🖥️ Dynamic terminal animation
* ⏱️ Controlled animation speed
* 🛑 Graceful exit with `Ctrl+C`

## 🛠️ Concepts Practiced

This project helped me practice:

* Dictionaries
* Lists
* Tuples
* Functions
* Loops
* Conditional statements
* Random number generation
* Terminal cursor positioning
* ANSI-style terminal colors through `bext`
* State management
* Simulation and animation
* Handling `KeyboardInterrupt`
* Working with external Python packages

## 📦 Requirement

This project uses the `bext` package to control the terminal cursor and colors.

Install it with:

```bash
pip install bext
```

## ▶️ How to Run

Run the program from the terminal:

```bash
python main.py
```

The terminal will display several colored `DVD` logos bouncing around the screen.

Press:

```text
Ctrl + C
```

to stop the animation.

## 🧠 What I Learned

This project was a fun introduction to thinking about **movement as changing state over time**. Instead of simply printing something once, the program continuously tracks each logo's position and direction, checks whether it has reached a boundary, updates its state, and redraws it. It was a nice little step toward understanding how simulations and animations can be built from relatively simple rules.

## 📚 Source

This project is based on a project from:

**The Big Book of Small Python Projects**
by **Al Sweigart**

It was implemented as part of my Python learning journey and used to practice simulation, state management, terminal manipulation, and working with external packages.
