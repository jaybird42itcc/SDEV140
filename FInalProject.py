"""
Author: Jacob Gamble
Date: May 8, 2025
Assignment: Final Project

My final project for this semester is a tkinter GUI rendition of the classic game Rock, Paper, Scissors.
The game is played by a player and the computer, and each choosing one of three options: rock, paper, or scissors.
The game ends when one player wins or there is a tie.
A new game is automatically started until the player clicks the Quit button.
The game is played using a random choice. A running total of wins and losses is displayed.

"""
# import

import tkinter as tk
import random

# Game logic and score counter

def Play(Choice):
    Options = ["Rock", "Paper", "Scissors"]
    ComputerChoice = random.choice(Options)

    global Score
    if Choice == ComputerChoice:
        Result = "It's a tie!"
    elif (Choice == "Rock" and ComputerChoice == "Scissors") or \
         (Choice == "Paper" and ComputerChoice == "Rock") or \
         (Choice == "Scissors" and ComputerChoice == "Paper"):
        Result = "You win!"
        Score += 1
    else:
        Result = "You lose!"

    ResultLabel.config(text=f"You chose {Choice}.\nComputer chose {ComputerChoice}.\n{Result}")
    ScoreLabel.config(text=f"{UserName}: {Score}")

# Start game window

def StartGame():
    global UserName
    UserName = NameEntry.get()
    if UserName.strip() == "":
        UserName = "Player"
    NameWindow.destroy()
    ShowMainWindow()

# GUI setup for name input

NameWindow = tk.Tk()
NameWindow.title("Enter Name")
NameWindow.geometry("300x100")

NameLabel = tk.Label(NameWindow, text="Enter your name:")
NameLabel.pack(pady=5)

NameEntry = tk.Entry(NameWindow)
NameEntry.pack(pady=5)

StartButton = tk.Button(NameWindow, text="Start Game", command=StartGame)
StartButton.pack(pady=5)

# Initialize score

Score = 0
UserName = ""

# Function to create main game window

def ShowMainWindow():
    global ResultLabel, ScoreLabel

    Root = tk.Tk()
    Root.title("Rock Paper Scissors")
    Root.geometry("350x300")

# Top frame for quit button

    TopFrame = tk.Frame(Root)
    TopFrame.pack(fill=tk.X, padx=10, pady=5)

    QuitButton = tk.Button(TopFrame, text="Quit", command=Root.destroy, fg="white", bg="red")
    QuitButton.pack(side=tk.RIGHT)

# Score display

    ScoreLabel = tk.Label(Root, text=f"{UserName}: {Score}", font=("Helvetica", 12))
    ScoreLabel.pack(pady=5)

# Buttons for Rock, Paper, Scissors

    ButtonFrame = tk.Frame(Root)
    ButtonFrame.pack(pady=10)

    RockButton = tk.Button(ButtonFrame, text="Rock", width=10, command=lambda: Play("Rock"))
    RockButton.grid(row=0, column=0, padx=5)

    PaperButton = tk.Button(ButtonFrame, text="Paper", width=10, command=lambda: Play("Paper"))
    PaperButton.grid(row=0, column=1, padx=5)

    ScissorsButton = tk.Button(ButtonFrame, text="Scissors", width=10, command=lambda: Play("Scissors"))
    ScissorsButton.grid(row=0, column=2, padx=5)

# Result label

    ResultLabel = tk.Label(Root, text="", font=("Helvetica", 12), pady=10)
    ResultLabel.pack()

    Root.mainloop()

# Start the name input loop

NameWindow.mainloop()
