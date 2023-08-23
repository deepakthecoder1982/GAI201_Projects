import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random

class RockPaperScissorsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors Game")
        self.root.geometry("600x400")

        self.user_score = 0
        self.computer_score = 0
        self.draw_score = 0

        self.create_ui()

    def create_ui(self):
        # Add UI components here
        self.user_label = ttk.Label(self.root, text="User: 0")
        self.computer_label = ttk.Label(self.root, text="Computer: 0")
        self.draw_label = ttk.Label(self.root, text="Draw: 0")

        self.user_label = ttk.Label(self.root, text="User: 0")
        self.computer_label = ttk.Label(self.root, text="Computer: 0")
        self.draw_label = ttk.Label(self.root, text="Draw: 0")
        
        self.result_label = ttk.Label(self.root, text="", font=("Helvetica", 14, "bold"))



def play(self, user_choice):
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    winner = self.determine_winner(user_choice, computer_choice)
    self.update_scores(winner)
    self.update_ui(user_choice, computer_choice, winner)

def determine_winner(self, user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "user"
    else:
        return "computer"


def play(self, user_choice):
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    winner = self.determine_winner(user_choice, computer_choice)
    self.update_scores(winner)
    self.update_ui(user_choice, computer_choice, winner)

def determine_winner(self, user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "user"
    else:
        return "computer"

def update_ui(self, user_choice, computer_choice, winner):
    self.result_label.config(
        text=f"Your choice: {user_choice.capitalize()}\nComputer's choice: {computer_choice.capitalize()}\n{winner.capitalize()} wins!",
        foreground="green" if winner == "user" else "red" if winner == "computer" else "black",
    )


def update_scores(self, winner):
    # Existing code...

    if self.user_score >= 3 or self.computer_score >= 3:
        self.end_game()

def end_game(self):
    if self.user_score > self.computer_score:
        winner = "User"
    elif self.user_score < self.computer_score:
        winner = "Computer"
    else:
        winner = "No one (It's a tie)"

    messagebox.showinfo("Game Over", f"{winner} wins the game!")
    self.root.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsApp(root)
    root.mainloop()
