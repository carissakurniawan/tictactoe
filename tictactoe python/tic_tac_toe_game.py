from tic_tac_toe_model import TicTacToe

def start_new_game():
    game = TicTacToe()
    against_computer = input("play against computer ? : (y/n) ")
    if against_computer == "y" or against_computer == "Y":
        game.play_game(True)
    elif against_computer == "n" or against_computer == "N":
        game.play_game(False)



start_new_game()