from tkinter import *
from tkinter import messagebox
import random

# Create the main window
root = Tk()
root.title("Tic-Tac-Toe")

# Define user-defined colors
bg_color = "white"
button_color = "light gray"
text_color = "black"

# Configure the window background color
root.configure(bg=bg_color)

# Create a list to represent the game board
board = [' ' for _ in range(9)]

# Variable to keep track of the current player
current_player = 'X'

# Function to handle a button click
def handle_click(index):
    global current_player
    if board[index] == ' ':
        # Update the game board
        board[index] = current_player
        buttons[index].config(text=current_player, state=DISABLED)
        # Check if the current player wins
        if check_winner(current_player):
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            reset_game()
        elif all(cell != ' ' for cell in board):
            messagebox.showinfo("Game Over", "It's a tie!")
            reset_game()
        else:
            # Switch the player
            current_player = 'O' if current_player == 'X' else 'X'
            # If the computer is playing, make a random move
            if current_player == 'O':
                computer_move()

# Function for the computer to make a move
def computer_move():
    available_moves = [index for index, cell in enumerate(board) if cell == ' ']
    if available_moves:
        random_index = random.choice(available_moves)
        handle_click(random_index)

# Function to check if a player wins
def check_winner(player):
    # Check rows
    for i in range(3):
        if board[i * 3] == board[i * 3 + 1] == board[i * 3 + 2] == player:
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == player:
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] == player or board[2] == board[4] == board[6] == player:
        return True
    return False

# Function to reset the game
def reset_game():
    global board, current_player
    board = [' ' for _ in range(9)]
    current_player = 'X'
    for button in buttons:
        button.config(text=' ', state=NORMAL)

# Create buttons for the game board
buttons = []
for i in range(9):
    button = Button(root, text=' ', font=('Arial', 24, 'bold'), width=6, height=3,
                    command=lambda index=i: handle_click(index), relief=RAISED, bg=button_color, fg=text_color)
    button.grid(row=i // 3, column=i % 3, padx=5, pady=5)
    buttons.append(button)

# Create a reset button
reset_button = Button(root, text="Reset", font=('Arial', 16), command=reset_game, bg=button_color, fg=text_color)
reset_button.grid(row=3, column=0, columnspan=3, pady=10)

# Start the main loop
root.mainloop()