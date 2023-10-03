import tkinter as tk
from tkinter import messagebox
import random


def determine_winner(player):
    choices = ["Rock", "Paper", "Scissors"]
    computer = random.choice(choices)
    message = f"And the Computer choses: {computer}\n"

    if player == computer:
        message += "Unluckily, It's a tie!"
    elif (player == "Rock" and computer == "Scissors") or \
         (player == "Paper" and computer == "Rock") or \
         (player == "Scissors" and computer == "Paper"):
        message += "Congrats!!! You win!"
    else:
        message += "Unfortunately, Computer wins!"

    messagebox.showinfo("RESULT ANNOUNCEMENT", message)


def reset_game():
    instruction.config(text="Select your choice:")
    play_again_button.pack_forget()


def choose_rock():
    determine_winner("Rock")
    instruction.config(text="Having fun? Let's Play Another round. Click Play Again")
    play_again_button.pack(pady=10)

def choose_paper():
    determine_winner("Paper")
    instruction.config(text="Having fun? Let's Play Another round. Click Play Again")
    play_again_button.pack(pady=10)

def choose_scissors():
    determine_winner("Scissors")
    instruction.config(text="Having fun? Let's Play Another round. Click Play Again")
    play_again_button.pack(pady=20)


game = tk.Tk()
game.geometry("400x500")
game.configure(bg="aqua")
game.title("Rock-Paper-Scissors Game")

manual=tk.Label(game,text="HOW TO PLAY: \n IN THIS GAME YOU HAVE THREE CHOICES ROCK,PAPER AND SCISSOR. \n\n WHO BEAT WHO? \n SCISSOR BEAT PAPER \n PAPER BEAT ROCK\n ROCK BEAT SCISSOR")
manual.pack(pady=30)
instruction = tk.Label(game, text="IN ORDER TO PLAY THE GAME \n Select your choice:")
instruction.pack(pady=20)


rock = tk.Button(game, text="Rock",width=50,bg="white",height=2, command=choose_rock)
rock.pack(pady=5)

paper = tk.Button(game, text="Paper",width=50,bg="white",height=2, command=choose_paper)
paper.pack(pady=5)

scissor = tk.Button(game, text="Scissors",width=50,bg="white",height=2, command=choose_scissors)
scissor.pack(pady=5)


play_again_button = tk.Button(game, text="Play Again",width=50,bg="white",height=2, command=reset_game)


game.mainloop()
