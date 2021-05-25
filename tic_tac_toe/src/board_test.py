from board import Board


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
