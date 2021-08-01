# Board Functions and Class


class Board:
    def __init__(self, dim):

        self.values = [None] * dim ** 2

        self.dim = dim

        self.template = ("|{}|{}|{}\n-------\n" * int(self.dim - 1)) + "|{}"*int(self.dim-1)

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

        else:
            return ((int(y)) * int(self.dim)) + (int(x))

    def render_board(self):
        """
        Renders the board in a way that the user can easily read it
        Returns
        -------
        string : The board rendered with an actual tic tac toe board template
        """
        # Print out the board, in a way humans can understand
        return self.template.format(*self.values)

    def validate_move(self, x, y):
        """
        Takes in a move as 2-dim coordinates, and a player, and validates that it is a valid move
        Parameters
        ----------
        x : integer
        The first of the two 2-dim coordinates to be operated on

        y : integer
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
        for row in range(0, board_width):
            values = set()
            for col in range(0, board_width):
                index = self.convert(row, col)
                if self.values[index] is not None:
                    values.add(self.values[index])
            
            if len(values) == 1:
                if x_or_o == next(iter(values)):
                    return True
        return False 

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
        for row in range(0, board_width):
            values = list()
            for col in range(0, board_width):
                index = self.convert(col, row)
                if self.values[index] is not None:
                    values.append(self.values[index])
            if len(values) == board_width and len(set(values)) == 1:
                if x_or_o == values[0]:
                    winner = True
                    breakpoint()
                    return winner
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
        values_rtl = set()
        values_ltr = set()
        for row in range(0, board_width):
            index_rtl = self.convert(row, row)
            index_ltr = self.convert(row, (-row + 2))
            values_rtl.add(self.values[index_rtl])
            values_ltr.add(self.values[index_ltr])
        if len(values_rtl) == 1:
            if x_or_o == list(values_rtl)[0]:
                winner = True
                return winner
            else:
                winner = False
        else:
            winner = False

        if len(values_ltr) == 1 and winner == False:
            if x_or_o == list(values_ltr)[0]:
                winner = True
                return winner
            else:
                winner = False
        else:
            winner = False

        return winner

    def check_winner(self, x_or_o):
        if self._check_column(x_or_o) == True:
            return True
        elif self._check_row(x_or_o) == True:
            return True
        elif self._check_diagonal(x_or_o) == True:
            return True
        else:
            return False
