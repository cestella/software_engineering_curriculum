from board_gen import Board


def test_3_x_row():
    board = Board(3)
    board.values[board.convert(0, 0)] = "X"
    board.values[board.convert(1, 0)] = "X"
    board.values[board.convert(2, 0)] = "X"
    assert board.check_winner("X") == True


def test_x_none_o_row():
    board = Board(3)
    board.values[board.convert(0, 0)] = "X"
    board.values[board.convert(1, 0)] = None
    board.values[board.convert(2, 0)] = "O"
    assert (
        board.check_winner("X") == False
        and board.check_winner("X") == False
    )


def test_3_none_row():
    board = Board(3)
    board.values[board.convert(0, 0)] = None
    board.values[board.convert(1, 0)] = None
    board.values[board.convert(2, 0)] = None
    assert (
        board.check_winner("X") == False
        and board.check_winner("O") == False
    )


def test_x_o_o_row():
    board = Board(3)
    board.values[board.convert(0, 0)] = "X"
    board.values[board.convert(1, 0)] = "O"
    board.values[board.convert(2, 0)] = "O"
    assert (
        board.check_winner("X") == False
        and board.check_winner("O") == False
    )


def test_full_board_row():
    board = Board(3)
    board.values = ["X", "X", "X", "X", "O", "X", None, None, None]
    assert (
        board.check_winner("X") == True and board.check_winner("O") == False
    )

def test_4x4_row():
    board = Board(4)
    board.values[board.convert(0,0)] = "X"
    board.values[board.convert(0,1)] = "X"
    board.values[board.convert(0,2)] = "X"
    board.values[board.convert(0,3)] = "X"
    assert (
        board.check_winner("X") == True
    )
    
def test_3_x_col():
    board = Board(3)
    board.values[board.convert(0, 0)] = "X"
    board.values[board.convert(0, 1)] = "X"
    board.values[board.convert(0, 2)] = "X"
    assert board.check_winner("X") == True


def test_x_none_o_col():
    board = Board(3)
    board.values[board.convert(0, 0)] = "X"
    board.values[board.convert(0, 1)] = None
    board.values[board.convert(0, 2)] = "O"
    assert (
        board.check_winner("X") == False
        and board.check_winner("O") == False
    )


def test_3_none_col():
    board = Board(3)
    board.values[board.convert(0, 0)] = None
    board.values[board.convert(0, 1)] = None
    board.values[board.convert(0, 2)] = None
    assert (
        board.check_winner("X") == False
        and board.check_winner("O") == False
    )


def test_x_o_o_col():
    board = Board(3)
    board.values[board.convert(0, 0)] = "X"
    board.values[board.convert(0, 1)] = "O"
    board.values[board.convert(0, 2)] = "O"
    assert (
        board.check_winner("X") == False
        and board.check_winner("O") == False
    )


def test_x_none_o_diag():
    board = Board(3)
    board.values[board.convert(0, 0)] = "X"
    board.values[board.convert(1, 1)] = None
    board.values[board.convert(2, 2)] = "O"

    assert board.check_winner("X") == True


def test_x_o_x_diag():
    board = Board(3)
    board.values[board.convert(0, 0)] = "X"
    board.values[board.convert(1, 1)] = "O"
    board.values[board.convert(2, 2)] = "X"
    assert (
        board.check_winner("X") == False
        and board.check_winner("O") == False
    )


def test_3_none_diag():
    board = Board(3)
    board.values[board.convert(0, 0)] = None
    board.values[board.convert(1, 1)] = None
    board.values[board.convert(2, 2)] = None
    assert (
        board.check_winner("X") == False
        and board.check_winner("O") == False
    )


def test_3_x_diag():
    board = Board(3)
    board.values[board.convert(0, 2)] = "X"
    board.values[board.convert(1, 1)] = "X"
    board.values[board.convert(2, 0)] = "X"
    assert (
        board.check_winner("X") == True and board.check_winner("O") == False
    )
"""
test_3_x_col()
test_x_none_o_col()
test_3_none_col()
test_x_o_o_col()

test_3_x_row()
test_x_none_o_row()
test_3_none_row()
test_x_o_o_row()
"""
# test_full_board_row()
# test_4x4_row()
 
test_x_none_o_diag()
#test_3_x_diag()
#test_3_none_diag()
#test_x_o_x_diag()

