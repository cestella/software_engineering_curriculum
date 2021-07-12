# Board Functions and Class


class Board:
    def __init__(self, dim):

        self.values = [None] * dim ** 2

        self.dim = dim

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

        for i in range(0, board_width):
            values = set()
            for j in range(0, board_width):
                index = index_fn(i,j) 
                if self.values[index] != None:
                    values.add(self.values[index])
            if len(values) == 1:
                if x_or_o == list(values)[0]:
                    winner = True
            else:
                winner = False
        print(winner)
        return winner

    def _check_column(self, x_or_o):
        return self.convert_abstraction(x_or_o, lambda x, y : self.convert(x, y))
        
    def _check_row(self, x_or_o):
        return self.convert_abstraction(x_or_o, lambda x, y : self.convert(y, x))

   
