import tkinter as tk
from tkinter import messagebox
import random

# Function to get the computer's choice
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

# Function to handle button click
def play_game(user_choice):
    # Get computer choice
    computer_choice = get_computer_choice()

    # Determine winner
    result = determine_winner(user_choice, computer_choice)

    # Show result in messagebox
    messagebox.showinfo("Game Result", f"You chose: {user_choice.capitalize()}\nComputer chose: {computer_choice.capitalize()}\n\nResult: {result}")

# Set up the main window
root = tk.Tk()
root.title("Rock Paper Scissors")

# Set up window size
root.geometry("300x300")

# Add a label to the window
label = tk.Label(root, text="Rock Paper Scissors", font=("Helvetica", 16))
label.pack(pady=20)

# Add buttons for user choices
rock_button = tk.Button(root, text="Rock", width=20, height=2, command=lambda: play_game("rock"))
rock_button.pack(pady=5)

paper_button = tk.Button(root, text="Paper", width=20, height=2, command=lambda: play_game("paper"))
paper_button.pack(pady=5)

scissors_button = tk.Button(root, text="Scissors", width=20, height=2, command=lambda: play_game("scissors"))
scissors_button.pack(pady=5)

# Run the application
root.mainloop()
