from board import Board


def validate_move_update():
    board = Board(3)
    board.values[0] = "X"
    return board


def test_3_x_row:
    board = Board(3)
    board.values[board.convert(0, 0)] = "X"
    board.values[board.convert(1, 0)] = "X"
    board.values[board.convert(2, 0)] = "X"
    assert board.check_winner("X", True) == True


def test_x_none_o_row():
    board = Board(3)
    board.values[board.convert(0, 0)] = "X"
    board.values[board.convert(1, 0)] = None
    board.values[board.convert(2, 0)] = "O"
    assert (
        board.check_winner("X", False) == True
        and board.check_winner("X", False) == True
    )


def test_3_none_row():
    board = Board(3)
    board.values[board.convert(0, 0)] = None
    board.values[board.convert(1, 0)] = None
    board.values[board.convert(2, 0)] = None
    assert (
        board.check_winner("X", False) == True
        and board.check_winner("O", False) == True
    )


def test_x_o_o_row():
    board = Board(3)
    board.values[board.convert(0, 0)] = "X"
    board.values[board.convert(1, 0)] = "O"
    board.values[board.convert(2, 0)] = "O"
    assert (
        board.check_winner("X", False) == True
        and board.check_winner("O", False) == True
    )


def test_full_board_row():
    board = Board(3)
    board.values = ["X", "X", "X", "X", "O", "X", None, None, None]
    assert (
        board.check_winner("X", True) == True and board.check_winner("O", False) == True
    )


def test_3_x_col():
    board = Board(3)
    board.values[board.convert(0, 0)] = "X"
    board.values[board.convert(0, 1)] = "X"
    board.values[board.convert(0, 2)] = "X"
    assert board.check_winner("X", True) == True


def test_x_none_o_col():
    board = Board(3)
    board.values[board.convert(0, 0)] = "X"
    board.values[board.convert(0, 1)] = None
    board.values[board.convert(0, 2)] = "O"
    assert (
        board.check_winner("X", False) == True
        and board.check_winner("O", False) == True
    )


def test_3_none_col():
    board = Board(3)
    board.values[board.convert(0, 0)] = None
    board.values[board.convert(0, 1)] = None
    board.values[board.convert(0, 2)] = None
    assert (
        board.check_winner("X", False) == True
        and board.check_winner("O", False) == True
    )


def test_x_o_o_col():
    board = Board(3)
    board.values[board.convert(0, 0)] = "X"
    board.values[board.convert(0, 1)] = "O"
    board.values[board.convert(0, 2)] = "O"
    assert (
        board.check_winner("X", False) == True
        and board.check_winner("O", False) == True
    )


def test_x_none_o_diag():
    board = Board(3)
    board.values[board.convert(0, 0)] = "X"
    board.values[board.convert(1, 1)] = None
    board.values[board.convert(2, 2)] = "O"

    assert board.check_winner("X", True) == True


def test_x_o_x_diag():
    board = Board(3)
    board.values[board.convert(0, 0)] = "X"
    board.values[board.convert(1, 1)] = "O"
    board.values[board.convert(2, 2)] = "X"
    assert (
        board.check_winner("X", False) == True
        and board.check_winner("O", False) == True
    )


def test_3_none_diag():
    board = Board(3)
    board.values[board.convert(0, 0)] = None
    board.values[board.convert(1, 1)] = None
    board.values[board.convert(2, 2)] = None
    assert (
        board.check_winner("X", False) == True
        and board.check_winner("O", False) == True
    )


def test_3_x_diag():
    board = Board(3)
    board.values[board.convert(0, 2)] = "X"
    board.values[board.convert(1, 1)] = "X"
    board.values[board.convert(2, 0)] = "X"
    assert (
        board.check_winner("X", True) == True and board.check_winner("O", False) == True
    )


def test_validate_move():
    board = validate_move_update()
    assert board.validate_move(0, 0) == False


test_column_1()
test_column_2()
test_column_3()
test_column_4()

test_row_1()
test_row_2()
test_row_3()
test_row_4()
test_row_5()

test_diagonal_1()
test_diagonal_2()
test_diagonal_3()
test_diagonal_4()

test_validate_move()
