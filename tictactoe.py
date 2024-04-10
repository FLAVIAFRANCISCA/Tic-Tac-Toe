import tkinter as tk
from tkinter import messagebox, simpledialog

class TicTacToeApp:
    def __init__(self, master):
        self.master = master
        master.title('Tic-Tac-Toe Enhanced')

        
        self.players = ["Player 1", "Player 2"]  
        self.scores = {self.players[0]: 0, self.players[1]: 0, "Draws": 0}
        self.current_player = 0  

      
        self.game_active = True
        self.board = [["" for _ in range(3)] for _ in range(3)]

       
        self.buttons = [[tk.Button(master, font=('Arial', 24), width=5, height=2,
                                   command=lambda r=r, c=c: self.button_click(r, c))
                         for c in range(3)] for r in range(3)]
        for r in range(3):
            for c in range(3):
                self.buttons[r][c].grid(row=r, column=c)

        self.status_label = tk.Label(master, text="", font=('Arial', 16))
        self.status_label.grid(row=3, column=0, columnspan=3)

        self.reset_button = tk.Button(master, text='Reset Game', command=self.reset_board)
        self.reset_button.grid(row=4, column=0, columnspan=3)

        
        self.register_players()
        self.update_status()

    def register_players(self):
        self.players[0] = simpledialog.askstring("Player Name", "Enter name for Player 1:")
        self.players[1] = simpledialog.askstring("Player Name", "Enter name for Player 2:")
        self.scores = {self.players[0]: 0, self.players[1]: 0, "Draws": 0}

    def button_click(self, r, c):
        if self.game_active and not self.board[r][c]:
            self.board[r][c] = "X" if self.current_player == 0 else "O"
            self.buttons[r][c].config(text="X" if self.current_player == 0 else "O")
            self.check_winner_or_draw()
            self.switch_player()

    def switch_player(self):
        self.current_player = 1 - self.current_player
        self.update_status()

    def update_status(self):
        if self.game_active:
            self.status_label.config(text=f"{self.players[self.current_player]}'s Turn")
        else:
            self.status_label.config(text="Game Over")

    def check_winner_or_draw(self):
        winner = None
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                winner = self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                winner = self.board[0][i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "" or \
           self.board[2][0] == self.board[1][1] == self.board[0][2] != "":
            winner = self.board[1][1]
        if winner:
            winner_name = self.players[0] if winner == "X" else self.players[1]
            messagebox.showinfo("Game Over", f"{winner_name} wins!")
            self.scores[winner_name] += 1
            self.game_active = False
        elif all(self.board[r][c] for r in range(3) for c in range(3)):
            messagebox.showinfo("Game Over", "It's a draw!")
            self.scores["Draws"] += 1
            self.game_active = False
        self.update_scoreboard()

    def update_scoreboard(self):
        scores_text = " | ".join([f"{player}: {score}" for player, score in self.scores.items()])
        self.status_label.config(text=scores_text)

    def reset_board(self):
        self.game_active = True
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for r in range(3):
            for c in range(3):
                self.buttons[r][c].config(text="")
        self.update_status()

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeApp(root)
    root.mainloop()
