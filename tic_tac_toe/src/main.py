# Main File
# Will hold the main control loop

# TODO:
# - Make lookup table for 2 value indexes, to machine available things

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
           
            lookup_table = {"['1', '1']":"0", "['1', '2']":"1", "['1', '3']":"2", "['2', '1']":"3", "['2', '2']":"4", "['3', '1']":"6", "['3', '2']":"7", "['3', '3']":"8"}    
 
            board.update(lookup_table[str(X_index_list)], "-1")

            if board.values[0] == -1:
                if board.values[1] == -1:
                    if board.values[2] == -1:
                        break

                if board.values[3] == -1:
                    if board.values[6] == -1:
                        break

                if board.values[4] == -1:
                    if board.values[8] == -1:
                        break

            if board.values[1] == -1:
                if board.values[4] == -1:
                    if board.values[7] == -1:
                        break

            if board.values[2] == -1:
                if board.values[5] == -1:
                    if board.values[8] == -1:
                        break

            if board.values[3] == -1:
                if board.values[4] == -1:
                    if board.values[5] == -1:
                        break

            if board.values[6] == -1:
                if board.values[7] == -1:
                    if board.values[8] == -1:
                        break

            if board.values[2] == -1:
                if board.values[4] == -1:       
                    if board.values[6] == -1:
                        break


            O_index_1 = input("Player 2, what is your first index?")
            O_index_2 = input("Player 2, what is your second index?")
            
            O_index_list = [str(O_index_1), str(O_index_2)]

            board.update(lookup_table[str(O_index_list)], "1")


            if board.values[0] == 1:
                if board.values[1] == 1:
                    if board.values[2] == 1:
                        game_over = True

                if board.values[3] == 1:
                    if board.values[6] == 1:
                        game_over = True

                if board.values[4] == 1:
                    if board.values[8] == 1:
                        game_over = True

            if board.values[1] == 1:
                if board.values[4] == 1:
                    if board.values[7] == 1:
                        game_over = True

            if board.values[2] == 1:
                if board.values[5] == 1:
                    if board.values[8] == 1:
                        game_over = True

            if board.values[3] == 1:
                if board.values[4] == 1:
                    if board.values[5] == 1:
                        game_over = True

            if board.values[6] == 1:
                if board.values[7] == 1:
                    if board.values[8] == 1:
                        game_over = True

            if board.values[2] == 1:
                if board.values[4] == 1:       
                    if board.values[6] == 1:
                        game_over = True


        print("Someone won!")

main()
