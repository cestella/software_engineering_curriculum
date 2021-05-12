# Board Representation

# test_board = [0, 1, -1, 0, 1, -1, 0, 1, -1]
# 9 values, for 9 spaces on the board
#
# -1 = X
# 0 = No Value
# 1 = O
#


class Board:
    def __init__(self):
        self.values = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.template = "{}|{}|{}\n-------\n{}|{}|{}\n-------\n{}|{}|{}"

    def render_board(self):
        return self.template.format(*self.values)

    def raw_board(self):
        return self.values

    def update(self, index, value):
        self.values[int(index)] = value
