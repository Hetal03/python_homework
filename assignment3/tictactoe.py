class TictactoeException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

class Board:
    valid_moves = [
        "upper left", "upper center", "upper right",
        "middle left", "center", "middle right",
        "lower left", "lower center", "lower right"
    ]

    def __init__(self):
        # 3x3 grid with " " in each cell
        self.board_array = [[" " for _ in range(3)] for _ in range(3)]
        self.turn = "X"
        self.last_move = None

    def __str__(self):
        lines = []
        lines.append(f" {self.board_array[0][0]} | {self.board_array[0][1]} | {self.board_array[0][2]} \n")
        lines.append("-----------\n")
        lines.append(f" {self.board_array[1][0]} | {self.board_array[1][1]} | {self.board_array[1][2]} \n")
        lines.append("-----------\n")
        lines.append(f" {self.board_array[2][0]} | {self.board_array[2][1]} | {self.board_array[2][2]} \n")
        return "".join(lines)

    def move(self, move_string):
        if move_string not in Board.valid_moves:
            raise TictactoeException("That's not a valid move.")

        move_index = Board.valid_moves.index(move_string)
        row = move_index // 3
        col = move_index % 3

        if self.board_array[row][col] != " ":
            raise TictactoeException("That spot is taken.")

        self.board_array[row][col] = self.turn
        self.last_move = (row, col)

        # Switch turn
        self.turn = "O" if self.turn == "X" else "X"

    def whats_next(self):
        # Check if board full
        cat = True
        for i in range(3):
            for j in range(3):
                if self.board_array[i][j] == " ":
                    cat = False
                    break
            if not cat:
                break
        if cat:
            return (True, "Cat's Game.")

        # Check rows for win
        for i in range(3):
            if (self.board_array[i][0] != " " and
                self.board_array[i][0] == self.board_array[i][1] == self.board_array[i][2]):
                return (True, f"{self.board_array[i][0]} wins!")

        # Check columns for win
        for i in range(3):
            if (self.board_array[0][i] != " " and
                self.board_array[0][i] == self.board_array[1][i] == self.board_array[2][i]):
                return (True, f"{self.board_array[0][i]} wins!")

        # Check diagonals for win
        if (self.board_array[1][1] != " " and
            ((self.board_array[0][0] == self.board_array[1][1] == self.board_array[2][2]) or
             (self.board_array[0][2] == self.board_array[1][1] == self.board_array[2][0]))):
            return (True, f"{self.board_array[1][1]} wins!")

        # Game not over, return whose turn it is
        return (False, f"{self.turn}'s turn.")

# Mainline game loop
if __name__ == "__main__":
    board = Board()
    print("Welcome to TicTacToe!")
    print(board)

    while True:
        finished, message = board.whats_next()
        if finished:
            print("Game over:", message)
            print(board)
            break
        else:
            print(message)
            move = input("Enter your move (e.g., 'upper left', 'center', 'lower right'): ").strip().lower()
            try:
                board.move(move)
                print(board)
            except TictactoeException as e:
                print(f"Error: {e.message}")