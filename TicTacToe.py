import tkinter as tk
from tkinter import messagebox
import random


class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Tic Tac Toe')

        self.board = ['' for _ in range(9)]  # game board, 9 spaces for 9 moves
        self.current_player = 'X'  # X will start the game
        self.computer_player = None  # Will hold 'X' or 'O' for the computer player

        # Create buttons
        self.buttons = [tk.Button(self.window, text='', font='Arial 20', height=2, width=5,
                                  command=lambda i=i: self.human_move(i)) for i in range(9)]
        # Arrange buttons in 3x3 grid
        for count, button in enumerate(self.buttons):
            row = count // 3
            col = count % 3
            button.grid(row=row, column=col)

        self.label = tk.Label(self.window, text="X's Turn", font='Arial 16')
        self.label.grid(row=3, column=0, columnspan=3)

        self.choose_player()

    def choose_player(self):
        choice = messagebox.askyesno("Choose your player", "Do you want to be X? (Yes for X, No for O)")
        if choice:
            self.computer_player = 'O'
        else:
            self.computer_player = 'X'
            self.computer_move()

    def human_move(self, position):
        if self.board[position] == '' and not self.game_over():
            self.board[position] = self.current_player
            self.buttons[position].config(text=self.current_player)
            if self.game_over():
                self.label.config(text=f'{self.current_player} Wins!')
                messagebox.showinfo("Game Over", f"{self.current_player} Wins!")
                self.window.quit()
            else:
                self.toggle_player()
                if self.current_player == self.computer_player:
                    self.computer_move()

    def computer_move(self):
        move = self.find_best_move()
        if move is not None:
            self.board[move] = self.computer_player
            self.buttons[move].config(text=self.computer_player)
            if self.game_over():
                self.label.config(text=f'{self.computer_player} Wins!')
                messagebox.showinfo("Game Over", f"{self.computer_player} Wins!")
                self.window.quit()
            else:
                self.toggle_player()

    def find_best_move(self):
        # If the computer can win in the next move, do it
        for i in range(9):
            if self.board[i] == '':
                self.board[i] = self.computer_player
                if self.game_over(True):
                    return i
                self.board[i] = ''  # Reset this space after checking

        # If the human player can win in the next move, block it
        human_player = 'O' if self.computer_player == 'X' else 'X'
        for i in range(9):
            if self.board[i] == '':
                self.board[i] = human_player
                if self.game_over(True):
                    return i
                self.board[i] = ''  # Reset this space after checking

        # Try to take one of the corners, if they are free
        corners = [0, 2, 6, 8]
        random.shuffle(corners)
        for i in corners:
            if self.board[i] == '':
                return i

        # Try to take the center, if it is free
        if self.board[4] == '':
            return 4

        # Move on one of the sides
        sides = [1, 3, 5, 7]
        random.shuffle(sides)
        for i in sides:
            if self.board[i] == '':
                return i

        return None

    def game_over(self, hypothetical=False):
        # Check if a player has won
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # horizontal
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),  # vertical
                                (0, 4, 8), (2, 4, 6)]  # diagonal
        for combination in winning_combinations:
            if self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]] != '':
                return True
        if not hypothetical and '' not in self.board:
            self.label.config(text='Tie!')
            messagebox.showinfo("Game Over", "It's a Tie!")
            self.window.quit()
        return False

    def toggle_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        self.label.config(text=f"{self.current_player}'s Turn")


if __name__ == "__main__":
    game = TicTacToe()
    game.window.mainloop()

