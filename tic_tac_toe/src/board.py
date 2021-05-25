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
        """
        converts a 2-dimensional coordinate to a 1-dimensional coordinate
        Parameters
        ----------
        x : integer or float
        the first of the two 2-dim coordinates to be operated on

        y : integer or float
        the first of the two 2-dim coordinates to be operated on

        Returns
        -------
        integer or float : the final 1-dim coordinate
        """
        if x < 0 or y < 0:
            return False

        elif x > 3 or y > 3:
            return False

        else:
            return ((y - 1) * int(self.dim)) + (x - 1)

    def render_board(self):
        """
        Renders the board in a way that the user can easily read it
        Returns
        -------
        string : The board rendered with an actual tic tac toe board template
        """

        # Print out the board, in a way humans can understand
        return self.template.format(*self.values)

    def raw_board(self):
        """
        Gives the raw list for the board
        Returns
        -------
        list : The curent state of the board in raw terms
        """
        return self.values

    def update_values(self, x, y, value):
        """
        Takes in a 2-dim coordinate and a value, and updates the value at that coordinate, in the list of values
        Parameters
        ----------
        x : integer or float
        The first of the two 2-dim coordinates to be operated on

        y : integer or float
        The first of the two 2-dim coordinates to be operated on

        Returns
        ---------
        value : string
        The value of which you want to update the given coordinate to
        """
        index = self._convert(x, y)

        self.values[int(index)] = value

    def get_value(self, x, y):
        """
        takes in a 2-dim coordinate and a value, and finds the value in that index
        Parameters
        ----------
        x : integer or float
        the first of the two 2-dim coordinates to be operated on

        y : integer or float
        the first of the two 2-dim coordinates to be operated on

        Returns
        ----------
        value : string
        the value that was given back when the function looked up those coordinates
        """
        return self.values[self._convert(x, y)]

    def get_move(self, player):
        """
        takes in a 2-dim coordinate and a value, and finds the value in that index
        parameters
        ----------
        x : integer or float
        the first of the two 2-dim coordinates to be operated on

        value : string
        the value that was given back when the function looked up those coordinates
        """
        index = input(
            "Player {player}, please put your move in, comma seperated, no spaces!"
        )

        index_list = list(index)

        return index_list

    def validate_move(self, x, y, player):
        """
        Takes in a move as 2-dim coordinates, and a player, and validates that it is a valid move
        Parameters
        ----------
        x : integer or float
        The first of the two 2-dim coordinates to be operated on

        y : integer or float
        The first of the two 2-dim coordinates to be operated on

        player : string
        "X" or "O", which player
        Returns
        ---------
        : boolean
        Whether or not it is a valid move
        """
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

    def check_column(self, board, x_or_o):
        """
        checks if a specific player has won with a column win
        parameters
        ----------
        board : class
        the board to operate on

        x_or_o : string
        which player we are checking for

        returns
        ----------
        winner : boolean
        whether or not that player won with a column win
        """
        board_width = 3
        winner = None

        for i in range(0, board_width):
            values = set()
            for j in range(0, board_width):
                index = self._convert(i, j)
                if board.values[index] != None:
                    values.add(board.values[index])
            if len(values) == 1:
                if x_or_o == list(values)[0]:
                    winner = True
                    break
                else:
                    winner = False
        return winner

    def check_row(self, board, x_or_o):
        """
        Checks if a specific player has won with a row win
        Parameters
        ----------
        board : class
        The board to operate on

        x_or_o : string
        Which player we are checking for

        Returns
        ----------
        winner : boolean
        Whether or not that player won with a row win
        """
        board_width = 3
        winner = None

        for i in range(0, board_width):
            values = set()
            for j in range(0, board_width):
                index = self._convert(i, j) + 1
                if board.values[index] != None:
                    values.add(board.values[index])
            if len(values) == 1:
                if x_or_o == list(values)[0]:
                    winner = True
                    break
                else:
                    winner = False
        return winner

    def check_diagonal(self, board, x_or_o):
        """
        Checks if a specific player has won with a diagonal win
        Parameters
        ----------
        board : class
        The board to operate on

        x_or_o : string
        Which player we are checking for

        Returns
        ----------
        winner : boolean
        Whether or not that player won with a diagonal win
        """

        # Check of someone has won

        board_width = 3
        winner = None

        if (
            board.values[0] == x_or_o
            and board.values[4] == x_or_o
            and board.values[8] == x_or_o
        ):
            winner = True
            return winner

        elif (
            board.values[2] == x_or_o
            and board.values[4] == x_or_o
            and board.values[6] == x_or_o
        ):
            winner = True
            return winner

        else:
            winner = False
            return winner


def update_column(board):
    board.update_values(3, 1, "X")
    board.update_values(3, 2, "X")
    board.update_values(3, 3, "X")


def update_diagonal(board):
    board.update_values(3, 3, "X")
    board.update_values(2, 2, "X")
    board.update_values(1, 1, "X")


def update_row(board):
    board.update_values(1, 3, "X")
    board.update_values(2, 3, "X")
    board.update_values(3, 3, "X")


def test_column(board):
    update_column(board)
    assert board.check_column(board, "X") == True


def test_row(board):
    update_row(board)
    assert board.check_row(board, "X") == True


def test_diagonal(board):
    update_diagonal(board)
    assert board.check_diagonal(board, "X") == True


board = Board(3)

test_column(board)
test_row(board)
test_diagonal(board)
