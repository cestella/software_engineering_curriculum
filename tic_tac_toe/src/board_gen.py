# Board Functions and Class


class Board:
    def __init__(self, dim):

        self.values = [None] * dim ** 2

        self.dim = dim
        
        self.template = ("|{}|{}|{}\n-------\n" * int(self.dim - 1)) + "|{}"*int(self.dim-1)

    def render_board(self):
        """
        Renders the board in a way that the user can easily read it
        Returns
        -------
        string : The board rendered with an actual tic tac toe board template
        """
        # Print out the board, in a way humans can understand
        return self.template.format(*self.values)

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
        return ((y) * int(self.dim)) + (x)

    def convert_abstraction(self, x_or_o, index_fn):
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
        values = set()
        for i in range(0, board_width):
            for j in range(0, board_width):
                index = index_fn(i, j)
                if self.values[index] != None:
                    values.add(self.values[index])
            print(values)
        if len(values) == 1:
            if x_or_o == list(values)[0]:
                print("odd")
                winner = True
                return winner
        else:
            winner = False
        return winner

    def _check_column(self, x_or_o):
        return self.convert_abstraction(x_or_o, lambda x, y: self.convert(x, y))

    def _check_row(self, x_or_o):
        return self.convert_abstraction(x_or_o, lambda x, y: self.convert(y, x))
    
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
