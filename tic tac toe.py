import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.reset_game()

    def reset_game(self):
        self.board = [None] * 9
        self.current_player = "X"
        self.buttons = []
        self.create_buttons()

    def create_buttons(self):
        for i in range(9):
            button = tk.Button(self.master, text="", font=('Arial', 24), width=5, height=2,
                               command=lambda i=i: self.make_move(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def make_move(self, index):
        if self.board[index] is None:
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif None not in self.board:
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # horizontal
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # vertical
            (0, 4, 8), (2, 4, 6)               # diagonal
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != None:
                return True
        return False

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()