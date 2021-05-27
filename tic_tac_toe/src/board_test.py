from board import Board


def update_column(board):
    board.values[board.convert(3, 1)] = "X"
    board.values[board.convert(3, 2)] = "X"
    board.values[board.convert(3, 3)] = "X"

def update_diagonal(board):
    board.values[board.convert(3, 3)] = "X"
    board.values[board.convert(2, 2)] = "X"
    board.values[board.convert(1, 1)] = "X"

def update_row(board):
    board.values[board.convert(1, 3)] = "X"
    board.values[board.convert(2, 3)] = "X"
    board.values[board.convert(3, 3)] = "X"

def validate_move_update(board):
    board.values[0] = "X"

def test_column(board):
    update_column(board)
    assert board.check_column(board, "X") == True


def test_row(board):
    update_row(board)
    assert board.check_row(board, "X") == True


def test_diagonal(board):
    update_diagonal(board)
    assert board.check_diagonal(board, "X") == True

def test_validate_move(board):
    validate_move_update(board)
    assert board.validate_move(1, 1, "X") == False

board = Board(3)

test_column(board)
test_row(board)
test_diagonal(board)
test_validate_move(board)
