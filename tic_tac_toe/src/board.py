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
        return ((x*int(self.dim))+y)-1

    def render_board(self):
        return self.template.format(*self.values)

    def raw_board(self):
        return self.values

    def update_values(self, x, y, value):

        index = self._convert(x, y)

        self.values[int(index)] = value

    def get_value(self, x, y):
        
        return self.values[self._convert(x, y)]

    def get_move(self, player):
        index = input("Player {player}, please put your move in, comma seperated, no spaces!")
    
        index_list = list(index) 
 
        return index_list

    def validate_move(self, x, y, player):
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


    def get_board_state(self, board):
       
         for i in range(0, int(self.dim)):
            x_row = 0
            o_row = 0
            for j in range(0, int(self.dim)):
                _index = self._convert(i, j)
                if self.values[int(_index)] == "X":
                    x_row += 1
                    
                if self.values[int(_index)] == "O":
                    o_row += 1

            if x_row == self.dim or o_row == self.dim:
                return "won"

board = Board(3)

print(board.render_board())
board.update_values(1, 1, "X")
board.update_values(1, 2, "X")
board.update_values(1, 3, "X")

print(board.render_board())
print(board.get_board_state(board))
