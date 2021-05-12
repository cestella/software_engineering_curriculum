# Main File
# Will hold the main control loop

# TODO:
# - Bug fix win detection

from board import Board


def main():

    playing = True

    while playing == True:
        print("You are playing Tic-Tac-Toe")
        print("P1 is X and P2 is O")

        board = Board()

        game_over = False

        while game_over == False:

            X_index_1 = input("Player 1, what is your first index?")
            X_index_2 = input("Player 1, what is your second index?")

            X_index_list = [str(X_index_1), str(X_index_2)]

            lookup_table = {
                "['1', '1']": "0",
                "['1', '2']": "1",
                "['1', '3']": "2",
                "['2', '1']": "3",
                "['2', '2']": "4",
                "['2', '3']": "5",
                "['3', '1']": "6",
                "['3', '2']": "7",
                "['3', '3']": "8",
            }

            who_won = None
            occupied_count = 0

            for e in board.values:
                if e != 0:
                    occupied_count += 1

                else:
                    break

            if occupied_count == 9:
                game_over = True
                who_won = "draw"

            occupied_count = 0

            board.update(int(lookup_table[str(X_index_list)]), -1)

            if board.values[0] == -1:
                if board.values[1] == -1:
                    if board.values[2] == -1:
                        game_over = True
                        who_won = "X"

                if board.values[3] == -1:
                    if board.values[6] == -1:
                        game_over = True
                        who_won = "X"

                if board.values[4] == -1:
                    if board.values[8] == -1:
                        game_over = True
                        who_won = "X"

            if board.values[1] == -1:
                if board.values[4] == -1:
                    if board.values[7] == -1:
                        game_over = True
                        who_won = "X"

            if board.values[2] == -1:
                if board.values[5] == -1:
                    if board.values[8] == -1:
                        game_over = True
                        who_won = "X"

            if board.values[3] == -1:
                if board.values[4] == -1:
                    if board.values[5] == -1:
                        game_over = True
                        who_won = "X"

            if board.values[6] == -1:
                if board.values[7] == -1:
                    if board.values[8] == -1:
                        game_over = True
                        who_won = "X"

            if board.values[2] == -1:
                if board.values[4] == -1:
                    if board.values[6] == -1:
                        game_over = True
                        who_won = "X"

            print(board.render_board())

            O_index_1 = input("Player 2, what is your first index?")
            O_index_2 = input("Player 2, what is your second index?")

            O_index_list = [str(O_index_1), str(O_index_2)]

            for e in board.values:

                if e != 0:
                    occupied_count += 1

                else:
                    break

            if occupied_count == 9:
                game_over = True
                who_won = "draw"

            board.update(lookup_table[str(O_index_list)], 1)

            if board.values[0] == 1:
                if board.values[1] == 1:
                    if board.values[2] == 1:
                        game_over = True
                        who_won = "O"

                if board.values[3] == 1:
                    if board.values[6] == 1:
                        game_over = True
                        who_won = "O"

                if board.values[4] == 1:
                    if board.values[8] == 1:
                        game_over = True
                        who_won = "O"

            if board.values[1] == 1:
                if board.values[4] == 1:
                    if board.values[7] == 1:
                        game_over = True
                        who_won = "O"

            if board.values[2] == 1:
                if board.values[5] == 1:
                    if board.values[8] == 1:
                        game_over = True
                        who_won = "O"

            if board.values[3] == 1:
                if board.values[4] == 1:
                    if board.values[5] == 1:
                        game_over = True
                        who_won = "O"

            if board.values[6] == 1:
                if board.values[7] == 1:
                    if board.values[8] == 1:
                        game_over = True
                        who_won = "O"

            if board.values[2] == 1:
                if board.values[4] == 1:
                    if board.values[6] == 1:
                        game_over = True
                        who_won = "O"

            print(board.render_board())

        if who_won == "X":
            print("Player 1 Won!")

        if who_won == "O":
            print("Player 2 Won!")

        if who_won == "draw":
            print("It was a draw!")

        play_again = input("If you want to play again, say yes, if not, say no!")

        if play_again == "yes":
            pass

        else:
            playing = False


main()
