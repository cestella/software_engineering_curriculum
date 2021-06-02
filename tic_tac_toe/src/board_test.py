from board import Board


def update_column_1(board):
    board.values[board.convert(3, 1)] = "X"
    board.values[board.convert(3, 2)] = "X"
    board.values[board.convert(3, 3)] = "X"

def update_column_2(board):
    board.values[board.convert(3, 1)] = "X"
    board.values[board.convert(3, 2)] = None
    board.values[board.convert(3, 3)] = "O"

def update_column_3(board):
    board.values[board.convert(3, 1)] = None
    board.values[board.convert(3, 2)] = None
    board.values[board.convert(3, 3)] = None

def update_column_4(board):
    board.values[board.convert(3, 1)] = "X"
    board.values[board.convert(3, 2)] = "O"
    board.values[board.convert(3, 3)] = "O"

def update_diagonal_1(board):
    board.values[board.convert(3, 3)] = "X"
    board.values[board.convert(2, 2)] = "X"
    board.values[board.convert(1, 1)] = "X"

def update_diagonal_2(board):
    board.values[board.convert(3, 3)] = "X"
    board.values[board.convert(2, 2)] = None
    board.values[board.convert(1, 1)] = "O"

def update_diagonal_3(board):
    board.values[board.convert(3, 3)] = "X"
    board.values[board.convert(2, 2)] = "O"
    board.values[board.convert(1, 1)] = "X"

def update_diagonal_4(board):
    board.values[board.convert(3, 3)] = None
    board.values[board.convert(2, 2)] = None
    board.values[board.convert(1, 1)] = None

def update_row_1(board):
    board.values[board.convert(1, 3)] = "X"
    board.values[board.convert(2, 3)] = "X"
    board.values[board.convert(3, 3)] = "X"

def update_row_2(board):
    board.values[board.convert(1, 3)] = "X"
    board.values[board.convert(2, 3)] = None
    board.values[board.convert(3, 3)] = "O"

def update_row_3(board):
    board.values[board.convert(1, 3)] = None
    board.values[board.convert(2, 3)] = None
    board.values[board.convert(3, 3)] = None

def update_row_4(board):
    board.values[board.convert(1, 3)] = "X"
    board.values[board.convert(2, 3)] = "O"
    board.values[board.convert(3, 3)] = "O"

def validate_move_update_1(board):
    board.values[0] = "X"

def test_column_1(board):
    update_column_1(board)
    assert board.check_winner("X") == True

def test_column_2(board):
    update_column_2(board)
    print(board.check_winner("X"), board.check_winner("O"))
    assert board.check_winner("X") == False and board.check_winner("O") == False

def test_column_3(board):
    update_column_3(board)
    print(board.check_winner("X"), board.check_winner("O"))
    assert board.check_winner("X") == False and board.check_winner("O") == False

def test_column_4(board):
    update_column_4(board)
    print(board.check_winner("X"), board.check_winner("O"))
    assert board.check_winner("X") == False and board.check_winner("O") == False

def test_row_1(board):
    update_row_1(board)
    assert board.check_winner("X") == True

def test_row_2(board):
    update_row_2(board)
    print(board.check_winner("X"), board.check_winner("O"))
    assert board.check_winner("X") == False and board.check_winner("O") == False

def test_row_3(board):
    update_row_3(board)
    print(board.check_winner("X"), board.check_winner("O"))
    assert board.check_winner("X") == False and board.check_winner("O") == False

def test_row_4(board):
    update_row_4(board)
    print(board.check_winner("X"), board.check_winner("O"))
    assert board.check_winner("X") == False and board.check_winner("O") == False

def test_diagonal_1(board):
    update_diagonal_1(board)
    assert board.check_winner("X") == True

def test_diagonal_2(board):
    update_diagonal_2(board)
    print(board.check_winner("X"), board.check_winner("O"))
    assert board.check_winner("X") == False and board.check_winner("O") == False

def test_diagonal_3(board):
    update_diagonal_3(board)
    print(board.check_winner("X"), board.check_winner("O"))
    assert board.check_winner("X") == False and board.check_winner("O") == False

def test_diagonal_4(board):
    update_diagonal_4(board)
    print(board.check_winner("X"), board.check_winner("O"))
    assert board.check_winner("X") == False and board.check_winner("O") == False


def test_validate_move_1(board):
    validate_move_update_1(board)
    assert board.validate_move(1, 1, "X") == False

def test_validate_move_2(board):
    assert board.validate_move(1, 1, "X") == True 



board = Board(3)
test_column_1(board)
board = Board(3)
#test_column_2(board)
board = Board(3)
test_column_3(board)
board = Board(3)
#test_column_4(board)
board = Board(3)
test_row_1(board)
board = Board(3)
#test_row_2(board)
board = Board(3)
test_row_3(board)
board = Board(3)
#test_row_4(board)
board = Board(3)
test_diagonal_1(board)
board = Board(3)
#test_diagonal_2(board)
board = Board(3)
#test_diagonal_3(board)
board = Board(3)
test_diagonal_4(board)
board = Board(3)
test_validate_move_1(board)
board = Board(3)
test_validate_move_2(board)
