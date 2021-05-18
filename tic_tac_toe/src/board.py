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
        return (x*int(self.dim))+y

    def render_board(self):
        return self.template.format(*self.values)

    def raw_board(self):
        return self.values

    def update_values(self, x, y, value):

        index = self._convert(x, y)

        self.values[int(index)] = value

    def get_value(self, x, y):
        
        1d = self._convert(x, y)

        return self.values[1d]

    def get_move(self, player):
        index = input("Player {player}, please put your move in, comma seperated, no spaces!")
    
        index_list = list(index) 
 
        return index_list

    def validate_move(self, x, y, player):
        1d_index = self._convert(x, y)

        if self.values[1d_index] == None:
            return True

        elif self.values[1d_index] == "X":
            if player == "X":
                return True

            elif player == "O":
                return False

        elif self.values[1d_index] == "O":
            if player == "O":
                return True

            elif player == "X":
                return False


    def get_board_state(self, board):
       
         for i in range(0, int(self.dim)):
            x_row = 0
            o_row = 0
            for j in range(0, int(self.dim)):
                1d_index = self._convert(i, j)
                if board[int(1d_index)] == "X":
                    x_row += 1
                    
                if board[int(1d_index)] == "O":
                    o_row += 1

            if x_row == self.dim or o_row == self.dim:
                return "won"
