# Board Representation

# test_board = [0, 1, -1, 0, 1, -1, 0, 1, -1]
# 9 values, for 9 spaces on the board
#
# -1 = X
# 0 = No Value
# 1 = O
#


class Board:
    def __init__(self, dim):
        self.values = [None, None, None, None, None, None, None, None, None]

        self.template = "{}|{}|{}\n-------\n{}|{}|{}\n-------\n{}|{}|{}"

        self.dim = dim

        self.winner = None

    def _convert(self, x, y):
        # Convert the 2 dimensional coordinates into 1d coords that we can use to subset the list of values
        if x < 0 or y < 0:
            return False

        elif x > 3 or y > 3:
            return False
    
        else:
            return (((y-1)*int(self.dim))+(x-1))


    def render_board(self):
        # Print out the board, in a way humans can understand
        return self.template.format(*self.values)

    def raw_board(self):
        # Print out the raw values of the board
        return self.values

    def update_values(self, x, y, value):
        # Update the value at a specific index
        index = self._convert(x, y)

        self.values[int(index)] = value

    def get_value(self, x, y):
        # Get the value at a specific index
        return self.values[self._convert(x, y)]

    def get_move(self, player):
        # Get the user input for a move from one user
        index = input("Player {player}, please put your move in, comma seperated, no spaces!")
    
        index_list = list(index) 
 
        return index_list

    def validate_move(self, x, y, player):
        # Check if move is a valid move
        _index = self._convert(x, y)

        if self.values[_index] == None:
            return True

        elif self.values[_index] == "X":
            if player == "X":
                return True

            elif player == "O":
                return False

        elif self.values[_index] == "O":
            if player == "O":
                return True

            elif player == "X":
                return False


    def check_won(self, board):
        # Check of someone has won      
 
        board_width = 3
        winner = None
        
        for i in range(0, board_width):
            values = set()
            for j in range(0, board_width):
                index = self._convert(i, j) + 1
                if board.values[index] != None:
                    values.add(board.values[index])
            if len(values) == 1:
                winner = list(values)[0]
                break
            return winner

        for i in range(0, board_width):
            values = set()
            for j in range(0, board_width):
                index = self._convert(j, i) + 1
                if board.values[index] != None:
                    values.add(board.values[index])
            if len(values) == 1:
                winner = list(values)[0]
                break
            return winner

        for i in range(0, board_width):
            values = set()
            for j in range(0, board_width):
                index = self._convert(j, i) + 1
                if board.values[index] != None:
                    values.add(board.values[index])
            if len(values) == 1:
                winner = list(values)[0]
                break
            return winner


def update_row(board):
    board.update_values(1, 1, "X")
    board.update_values(1, 2, "X")
    board.update_values(1, 3, "X")

def update_diagonal(board):
    board.update_values(1, 1, "X")
    board.update_values(2, 2, "X")
    board.update_values(3, 3, "X")

def update_column(board):
    board.update_values(1, 1, "X")
    board.update_values(2, 1, "X")
    board.update_values(3, 1, "X")

board = Board(3)

print(board.render_board())
update_column(board)

print(board.render_board())
print(board.check_won(board))

