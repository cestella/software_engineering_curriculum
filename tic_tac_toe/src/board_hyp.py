# Board Functions and Class


class Board:
    def __init__(self, dim):

        self.values = [None] * dim ** 2

        self.dim = dim

        self.template = ("{}|{}|{}\n-------\n" * int(self.dim - 1)) + "{}|{}|{}"

        self.winner = None

    def convert(self, x, y):
        """
        converts a 2-dimensional coordinate to a 1-dimensional coordinate
        Parameters
        ----------
        x : integer
        the first of the two 2-dim coordinates to be operated on

        y : integer
        the first of the two 2-dim coordinates to be operated on

        Returns
        -------
        integer: the final 1-dim coordinate
        """
        if x < 0 or y < 0:
            raise ValueError("Not Proper Inputs")

        elif x > 2 or y > 2:
            raise ValueError("Not Proper Inputs")

        else:
            return ((y) * int(self.dim)) + (x)

    def render_board(self):
        """
        Renders the board in a way that the user can easily read it
        Returns
        -------
        string : The board rendered with an actual tic tac toe board template
        """
        # Print out the board, in a way humans can understand
        return self.template.format(*self.values)

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
        return self.values[self.convert(x, y)] == None

    def _check_column(self, x_or_o):
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
        board_width = self.dim
        winner = None

        for i in range(0, board_width):
            values = set()
            for j in range(0, board_width):
                index = self.convert(i, j)
                if self.values[index] != None:
                    values.add(self.values[index])
            if len(values) == 1:
                if x_or_o == list(values)[0]:
                    winner = True
            else:
                winner = False
        return winner

    def _check_row(self, x_or_o):
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
        board_width = self.dim
        winner = None
        for i in range(0, board_width):
            values = set()
            for j in range(0, board_width):
                index = self.convert(j, i)
                if self.values[index] != None:
                    values.add(self.values[index])
            if len(values) == 1:
                if x_or_o == list(values)[0]:
                    winner = True
            else:
                winner = False
        return winner

    def _check_diagonal(self, x_or_o):
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
        board_width = self.dim
        winner = None
        values = set()
        values2 = set()
        for i in range(0, board_width):
            index = self.convert(i, i)
            index2 = self.convert(i, (-i + 2))
            values.add(self.values[index])
            values2.add(self.values[index2])
        if len(values) == 1:
            if x_or_o == list(values)[0]:
                winner = True
                return winner
            else:
                winner = False
        else:
            winner = False

        if len(values2) == 1 and winner == False:
            if x_or_o == list(values2)[0]:
                winner = True
                return winner
            else:
                winner = False
        else:
            winner = False
        return winner

    def check_winner(self, x_or_o, tof):
        if self._check_column(x_or_o) == tof:
            return True
        elif self._check_row(x_or_o) == tof:
            return True
        elif self._check_diagonal(x_or_o) == tof:
            return True
        else:
            return False
