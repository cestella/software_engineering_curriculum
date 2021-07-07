from board import Board

def validate_move_update():
    board = Board(3)
    board.values[0] = "X"
    return board


def test_column_1():
    board = Board(3)
    board.values[board.convert(0, 0)] = "X"
    board.values[board.convert(1, 0)] = "X"
    board.values[board.convert(2, 0)] = "X"
    assert board.check_winner("X", True) == True


def test_column_2():
    board = Board(3)
    board.values[board.convert(0, 0)] = "X"
    board.values[board.convert(1, 0)] = None
    board.values[board.convert(2, 0)] = "O"
    assert (
        board.check_winner("X", False) == True
        and board.check_winner("X", False) == True
    )


def test_column_3():
    board = Board(3)
    board.values[board.convert(0, 0)] = None
    board.values[board.convert(1, 0)] = None
    board.values[board.convert(2, 0)] = None
    assert (
        board.check_winner("X", False) == True
        and board.check_winner("O", False) == True
    )


def test_column_4():
     board = Board(3)
    board.values[board.convert(0, 0)] = "X"
    board.values[board.convert(1, 0)] = "O"
    board.values[board.convert(2, 0)] = "O"
    assert (
        board.check_winner("X", False) == True
        and board.check_winner("O", False) == True
    )


def test_row_1():
    board = Board(3)
    board.values[board.convert(0, 0)] = "X"
    board.values[board.convert(0, 1)] = "X"
    board.values[board.convert(0, 2)] = "X"
    assert board.check_winner("X", True) == True


def test_row_2():
    board = Board(3)
    board.values[board.convert(0, 0)] = "X"
    board.values[board.convert(0, 1)] = None
    board.values[board.convert(0, 2)] = "O"
    assert (
        board.check_winner("X", False) == True
        and board.check_winner("O", False) == True
    )


def test_row_3():
    board = Board(3)
    board.values[board.convert(0, 0)] = None
    board.values[board.convert(0, 1)] = None
    board.values[board.convert(0, 2)] = None
    assert (
        board.check_winner("X", False) == True
        and board.check_winner("O", False) == True
    )


def test_row_4():
    board = Board(3)
    board.values[board.convert(0, 0)] = "X"
    board.values[board.convert(0, 1)] = "O"
    board.values[board.convert(0, 2)] = "O"
    assert (
        board.check_winner("X", False) == True
        and board.check_winner("O", False) == True
    )


def test_diagonal_1():
    board = Board(3)
    board.values[board.convert(0, 0)] = "X"
    board.values[board.convert(1, 1)] = None
    board.values[board.convert(2, 2)] = "O"

    assert board.check_winner("X", True) == True


def test_diagonal_2():
    board = Board(3)
    board.values[board.convert(0, 0)] = "X"
    board.values[board.convert(1, 1)] = "O"
    board.values[board.convert(2, 2)] = "X"
    assert (
        board.check_winner("X", False) == True
        and board.check_winner("O", False) == True
    )


def test_diagonal_3():
    board = Board(3)
    board.values[board.convert(0, 0)] = None
    board.values[board.convert(1, 1)] = None
    board.values[board.convert(2, 2)] = None
    assert (
        board.check_winner("X", False) == True
        and board.check_winner("O", False) == True
    )

def test_diagonal_4():
    board = Board(3)
    board.values[board.convert(0, 2)] = "X"
    board.values[board.convert(1, 1)] = "X"
    board.values[board.convert(2, 0)] = "X"
    assert (
        board.check_winner("X", True) == True and board.check_winner("O", False) == True
    )


def test_validate_move():
    board = validate_move_update()
    assert board.validate_move(0, 0, "X") == False


test_column_1()
test_column_2()
test_column_3()
test_column_4()

test_row_1()
test_row_2()
test_row_3()
test_row_4()

test_diagonal_1()
test_diagonal_2()
test_diagonal_3()
test_diagonal_4()

test_validate_move_1()
