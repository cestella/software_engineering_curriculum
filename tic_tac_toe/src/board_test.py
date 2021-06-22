from board import Board


def update_column_1():
    board = Board(3)
    board.values[board.convert(0, 0)] = "X"
    board.values[board.convert(1, 0)] = "X"
    board.values[board.convert(2, 0)] = "X"
    return board


def update_column_2():
    board = Board(3)
    board.values[board.convert(0, 0)] = "X"
    board.values[board.convert(1, 0)] = None
    board.values[board.convert(2, 0)] = "O"
    return board


def update_column_3():
    board = Board(3)
    board.values[board.convert(0, 0)] = None
    board.values[board.convert(1, 0)] = None
    board.values[board.convert(2, 0)] = None
    return board


def update_column_4():
    board = Board(3)
    board.values[board.convert(0, 0)] = "X"
    board.values[board.convert(1, 0)] = "O"
    board.values[board.convert(2, 0)] = "O"
    return board


def update_diagonal_1():
    board = Board(3)
    board.values[board.convert(0, 0)] = "X"
    board.values[board.convert(1, 1)] = "X"
    board.values[board.convert(2, 2)] = "X"
    return board


def update_diagonal_2():
    board = Board(3)
    board.values[board.convert(0, 0)] = "X"
    board.values[board.convert(1, 1)] = None
    board.values[board.convert(2, 2)] = "O"
    return board


def update_diagonal_3():
    board = Board(3)
    board.values[board.convert(0, 0)] = "X"
    board.values[board.convert(1, 1)] = "O"
    board.values[board.convert(2, 2)] = "X"
    return board


def update_diagonal_4():
    board = Board(3)
    board.values[board.convert(0, 0)] = None
    board.values[board.convert(1, 1)] = None
    board.values[board.convert(2, 2)] = None
    return board


def update_diagonal_5():
    board = Board(3)
    board.values[board.convert(0, 2)] = "X"
    board.values[board.convert(1, 1)] = "X"
    board.values[board.convert(2, 0)] = "X"
    return board


def update_row_1():
    board = Board(3)
    board.values[board.convert(0, 0)] = "X"
    board.values[board.convert(0, 1)] = "X"
    board.values[board.convert(0, 2)] = "X"
    return board


def update_row_2():
    board = Board(3)
    board.values[board.convert(0, 0)] = "X"
    board.values[board.convert(0, 1)] = None
    board.values[board.convert(0, 2)] = "O"
    return board


def update_row_3():
    board = Board(3)
    board.values[board.convert(0, 0)] = None
    board.values[board.convert(0, 1)] = None
    board.values[board.convert(0, 2)] = None
    return board


def update_row_4():
    board = Board(3)
    board.values[board.convert(0, 0)] = "X"
    board.values[board.convert(0, 1)] = "O"
    board.values[board.convert(0, 2)] = "O"
    return board


def validate_move_update_1():
    board = Board(3)
    board.values[0] = "X"
    return board


def test_column_1():
    board = update_column_1()
    assert board.check_winner("X", True) == True


def test_column_2():
    board = update_column_2()
    assert (
        board.check_winner("X", False) == True
        and board.check_winner("X", False) == True
    )


def test_column_3():
    board = update_column_3()
    assert (
        board.check_winner("X", False) == True
        and board.check_winner("O", False) == True
    )


def test_column_4():
    board = update_column_4()
    assert (
        board.check_winner("X", False) == True
        and board.check_winner("O", False) == True
    )


def test_row_1():
    board = update_row_1()
    assert board.check_winner("X", True) == True


def test_row_2():
    board = update_row_2()
    assert (
        board.check_winner("X", False) == True
        and board.check_winner("O", False) == True
    )


def test_row_3():
    board = update_row_3()
    assert (
        board.check_winner("X", False) == True
        and board.check_winner("O", False) == True
    )


def test_row_4():
    board = update_row_4()
    assert (
        board.check_winner("X", False) == True
        and board.check_winner("O", False) == True
    )


def test_diagonal_1():
    board = update_diagonal_1()
    assert board.check_winner("X", True) == True


def test_diagonal_2():
    board = update_diagonal_2()
    assert (
        board.check_winner("X", False) == True
        and board.check_winner("O", False) == True
    )


def test_diagonal_3():
    board = update_diagonal_3()
    assert (
        board.check_winner("X", False) == True
        and board.check_winner("O", False) == True
    )


def test_diagonal_4():
    board = update_diagonal_4()
    assert (
        board.check_winner("X", False) == True
        and board.check_winner("O", False) == True
    )


def test_diagonal_5():
    board = update_diagonal_5()
    assert (
        board.check_winner("X", True) == True and board.check_winner("O", False) == True
    )


def test_validate_move_1():
    board = validate_move_update_1()
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
test_diagonal_5()

test_validate_move_1()
