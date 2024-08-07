# Core game model here. Define your namedtuple to represent your game state.
# All functions should be pure i.e. no i/o, no global vars etc.

from tic_tac_toe_move_exception import InvalidKeyException, InvalidMoveException
import random

# Print the game board

class TicTacToe:

    def __init__(self): #initialised board
        self._board = {"1": ' ', "2": ' ' , "3": ' ',
        "4": ' ', "5": ' ', "6": ' ',
        "7": ' ', "8": ' ', "9": ' '} 

        self._game_running = True
        self._current_player = "X"      
        self._count = 0  
        self._board_keys = []
        self._tie = False

        for key in self._board:
            self._board_keys.append(key)

        
    def print_board(self):
        print("---------")
        print(self._board['1'] + " | " + self._board['2'] + " | " + self._board['3'])
        print("---------")
        print(self._board['4'] + " | " + self._board['5'] + " | " + self._board['6'])
        print("---------")
        print(self._board['7'] + " | " + self._board['8'] + " | " + self._board['9'])
        print("---------")

    def game_over(self):
        self.print_board ()
        print("\nGame Over.\n")
        if self._tie == False:                
            print(" **** " + self._current_player + " won. ****")   

    def is_winner(self):
        if self._count >= 5:
            if self._board['1'] == self._board['2'] == self._board['3'] != ' ': # across the top           
                return True
            elif self._board['4'] == self._board['5'] == self._board['6'] != ' ': # across the middle
                return True
            elif self._board['7'] == self._board['8'] == self._board['9'] != ' ': # across the bottom
                return True
            elif self._board['1'] == self._board['4'] == self._board['7'] != ' ': # down the left side
                return True
            elif self._board['2'] == self._board['5'] == self._board['8'] != ' ': # down the middle
                return True
            elif self._board['3'] == self._board['6'] == self._board['9'] != ' ': # down the right side
                return True
            elif self._board['1'] == self._board['5'] == self._board['9'] != ' ': # diagonal
                return True
            elif self._board['3'] == self._board['5'] == self._board['7'] != ' ': # diagonal
                return True
            else:
                return False

    def valid_move(self, move): # valid move is when the cell is empty (means place has not been taken by other players)
        try:
            if not str.isdigit(move) or move == "0" or int(move) > 9:
                raise InvalidKeyException
            return self._board[move] == ' ' #True or False
        except InvalidKeyException:
            print("That key is not valid. Try again within 1-9 range!")
            return False #False

    def computer_turn(self): 
        print("computer_move")
        turn_finish = False 
        while turn_finish == False:
            print("computer trying to take a move")
            move = str(random.randint(1,9)) #thats why we need str here to change the computer input into string not an integer cause it will create error if it's integer.
            if self.valid_move(move): # check if it's a valid move (empty cell).
                self.update_turn(move)
                turn_finish = True
            else:
                if not str.isdigit(move) or move == "0" or int(move) > 9:
                    return
                else:
                    print("That place has been taken by other players. Please enter other number.")


    def human_turn(self):
        turn_finish = False
        while turn_finish == False:
            self.print_board()
            print("It's your turn, " + self._current_player + " . Enter number 1-9: ")
            move = input() # python input is always a string
            if self.valid_move(move): # check if it's a valid move (empty cell).
                self.update_turn(move)
                turn_finish = True # finish filling 9 box
            else:
                if not str.isdigit(move) or move == "0" or int(move) > 9:
                    pass
                else:
                    print ("That place has been taken by other players. Please enter other number.")

    def update_turn(self, move):
        if self.valid_move(move):
            self._board[move] = self._current_player 
            self._count += 1
            #if self._count != 0: # if this not a first turn
            if self._current_player =='X':
                self._current_player = 'O'
            else:
                self._current_player = 'X'         
        else:
            raise InvalidMoveException

    def play_game(self, against_computer):
        while self._game_running == True:
            print("the current turn is" + str(self._count))
            if against_computer and self._current_player == "O":
                self.computer_turn()
            else:
                self.human_turn()
            
            if self.is_winner():
                self._game_running = False
                self.game_over()
                continue #stop here, dont continue to next code. continue stops the current step and continue to else.
            #pass stop entire function, break stops entire loops, 

            if self._count == 9: #because it's start from 0, so this means the 9th turn
                self._tie = True
                print("It's a tie!")
                self._game_running = False
                self.print_board()

        else:
            restart = input("Wanna play again : (y/n) ")
            if restart == "y" or restart == "Y": 
                start_new_game()
            else:
                print("Game Over. Thank you for playing!")

def start_new_game():
    game = TicTacToe()
    against_computer = input("play against computer ? : (y/n) ")
    if against_computer == "y" or against_computer == "Y":
        game.play_game(True)
    elif against_computer == "n" or against_computer == "N":
        game.play_game(False)