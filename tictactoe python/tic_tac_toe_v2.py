# THIS IS A DRAFT AND TRIAL ERROR



from tic_tac_toe_move_exception import InvalidInputException, is_valid
import random


# Make the board

board = {"1": ' ', "2": ' ' , "3": ' ',
        "4": ' ', "5": ' ', "6": ' ',
        "7": ' ', "8": ' ', "9": ' '}

board_keys = []

for key in board:
    board_keys.append(key)

game_running = True
current_player = "X"

# Print the game board


def print_board(board):
    print("---------")
    print(board['1'] + " | " + board['2'] + " | " + board['3'])
    print("---------")
    print(board['4'] + " | " + board['5'] + " | " + board['6'])
    print("---------")
    print(board['7'] + " | " + board['8'] + " | " + board['9'])
    print("---------")

def game_over():
     print("\nGame Over.\n")
     print(" **** " + current_player + " won. ****")    


#The game
def game():
    game_running = True
    current_player = 'X'
    count = 0
    
    while game_running:
            print_board(board)
            print("It's your turn, " + current_player + " . Enter number 1-9: ")

            move = input()        
            
            if board[move] == ' ':
                board[move] = current_player
                count += 1
            else:
                print("That place has been taken by other players. Please enter other number.")
                continue
            
            if count >= 5:
                if board['1'] == board['2'] == board['3'] != ' ': # across the top
                    print_board (board)
                    print("\nGame Over.\n")                
                    print(" **** " + current_player + " won. ****")                
                    break
                elif board['4'] == board['5'] == board['6'] != ' ': # across the middle
                    print_board (board)
                    print("\nGame Over.\n")                
                    print(" **** " + current_player + " won. ****")
                    break
                elif board['7'] == board['8'] == board['9'] != ' ': # across the bottom
                    print_board (board)
                    print("\nGame Over.\n")                
                    print(" **** " + current_player + " won. ****")
                    break
                elif board['1'] == board['4'] == board['7'] != ' ': # down the left side
                    print_board (board)
                    print("\nGame Over.\n")                
                    print(" **** " + current_player + " won. ****")
                    break
                elif board['2'] == board['5'] == board['8'] != ' ': # down the middle
                    print_board (board)
                    print("\nGame Over.\n")                
                    print(" **** " + current_player + " won. ****")
                    break
                elif board['3'] == board['6'] == board['9'] != ' ': # down the right side
                    print_board (board)
                    print("\nGame Over.\n")                
                    print(" **** " + current_player + " won. ****")
                    break 
                elif board['1'] == board['5'] == board['9'] != ' ': # diagonal
                    print_board (board)
                    print("\nGame Over.\n")                
                    print(" **** " + current_player + " won. ****")
                    break
                elif board['3'] == board['5'] == board['7'] != ' ': # diagonal
                    print_board (board)
                    print("\nGame Over.\n")                
                    print(" **** " + current_player + " won. ****")
                    break 

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
            if count == 9:
                print("Game Over.")                
                print("It's a Tie!!")

        # we have to change the player after every move.
            if current_player =='X':
                current_player = 'O'
            else:
                current_player = 'X'
                
    restart = input("Do you want to play again ? (y/n) :" )
    if restart == "y" or restart == "Y":
        for key in board_keys:
            board[key] = " "
        game()

    else:
        print("Game Over")

#if __name__ == "__main__":
#    game()
        

def computer(board):
    while current_player == "O":
        move = random.randint(1,9)
        if board[move] == " ":
            board[move] = "O"
        elif current_player == "X":
            current_player = "O"
        else:
            current_player = "X"


game()
    #computer(board)restart()


from tic_tac_toe_move_exception import InvalidInputException, is_valid
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
        return self._board[move] == ' '


    def take_turn(self, computer):
        if self._count != 0: # if this not a first turn
            if self._current_player =='X':
                self._current_player = 'O'
            else:
                self._current_player = 'X' 

        if computer == False: # it means if play with friends

            self.print_board()
            print("It's your turn, " + self._current_player + " . Enter number 1-9: ")
            move = input()  

            if self.valid_move(move): # check if it's a valid move (empty cell).
                self._board[move] = self._current_player
                self._count += 1 # if its an empty cell, players and put a sign on it.

            else:
                print("That place has been taken by other players. Please enter other number.")

        else:
            print("computer_move")
            computer_move = True 
            while computer_move == True:
                print("computer trying to take a move")
                move = random.randint(1,9)
                if self.valid_move(move): # check if it's a valid move (empty cell).
                    print("computer found valid move")
                    self._board[move] = self._current_player
                    self._count += 1 # if its an empty cell, players and put a sign on it.
                    computer_move = False
                else:
                    print("computer found invalid move")

    def play_game(self, against_computer):
        while self._game_running == True:
            self.take_turn(self._current_player == "X" and self._count != 0)
            if self.is_winner():
                self._game_running = False
                self.game_over()
        
        else:
            restart = input("Wanna play again : (y/n) ")
            against_computer = input("with friends (y) or with computer (n) : (y/n)")
            if restart == "y" or restart == "Y": 
                start_new_game()
            else:
                print("Game Over")



def start_new_game():
    game = TicTacToe()
    against_computer = input("play against computer ? : (y/n) ")
    if against_computer == "y" or against_computer == "Y":
        game.play_game(True)
    elif against_computer == "n" or against_computer == "N":
        game.play_game(False)



start_new_game()


import os
import unittest
from unittest.mock import patch
from io import StringIO
from tic_tac_toe_model import Board
from tic_tac_toe_game import Computer, Game
from tic_tac_toe_save_load import save_obj, load_obj

from tic_tac_toe_move_exception import InvalidKeyException


class BoardTestCases(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_update(self):
        pos, value = 1, "X"
        self.board.update(pos, value)
        self.assertEqual(str(self.board), str(dict(zip([i for i in range(1, 10)], [
            "X", " ", " ", " ", " ", " ", " ", " ", " "]))))

        pos, value = 9, "O"
        self.board.update(pos, value)
        self.assertEqual(str(self.board), str(dict(zip([i for i in range(1, 10)], [
            "X", " ", " ", " ", " ", " ", " ", " ", "O"]))))

        with self.assertRaises(InvalidKeyException):
            self.board.update(11, "X")

    @patch('sys.stdout', new_callable=StringIO)
    def test_render(self, stdout):
        self.board.update(1, "X")
        self.board.update(5, "O")
        self.board.update(9, "X")

        visual = "X| | \n-+-+-\n |O| \n-+-+-\n | |X\n"
        self.board.render()
        self.assertEqual(stdout.getvalue(), visual)

    def test_board_won(self):
        self.board.update(1, "X")
        self.board.update(2, "X")
        self.board.update(3, "X")

        self.assertTrue(self.board.check_board_won())

        self.board.update(2, "O")
        self.board.update(5, "O")
        self.board.update(8, "O")

        self.assertTrue(self.board.check_board_won())

        self.board.update(1, "X")
        self.board.update(5, "X")
        self.board.update(9, "X")

        self.assertTrue(self.board.check_board_won())

        self.board.update(1, "X")
        self.board.update(5, "O")
        self.board.update(9, "X")

        self.assertTrue(self.board.check_board_won())

        self.board.update(1, " ")
        self.board.update(5, " ")
        self.board.update(9, " ")

        self.assertFalse(self.board.check_board_won())

    def test_valid_move(self):
        self.board.update(5, "X")

        self.assertFalse(self.board.valid_move(5))
        self.assertTrue(self.board.valid_move(8))

        with self.assertRaises(KeyError):
            self.board.valid_move(10)
            self.board.valid_move("X")


class ComputerTestCases(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.computer = Computer(MARKER="O")

    def test_check_win_possible(self):
        self.board.update(1, "X")
        self.board.update(2, "X")

        possible = [k for (k, v) in self.board.board.items() if v == " "]
        player = "X"

        self.assertTrue(self.computer.check_win_possible(
            possible, self.board, player))

        self.board.update(1, "X")
        self.board.update(2, " ")
        self.board.update(6, "X")

        self.assertFalse(self.computer.check_win_possible(
            possible, self.board, player))


class IOTestCases(unittest.TestCase):

    def setUp(self):
        self.game = Game(computer=True)

    def test_save_obj(self):
        save_obj(self.game, ".test_save.pickle")

        self.assertTrue(os.path.exists(".test_save.pickle"))

    def test_load_obj(self):
        save_obj(self.game, ".test_save.pickle")

        self.assertTrue(load_obj(".test_save.pickle"))

    def tearDown(self):
        os.system("rm .test_save.pickle")


if __name__ == "__main__":
    unittest.main()


# PLAYING WITH COMPUTER

from tic_tac_toe_move_exception import InvalidInputException

# Make the board

board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

current_player = "X"
winner = None
game_running = True

# Print the game board
def print_board(board):
    print("---------")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("---------")

# Player Input
def player_input(board):
    inp = int(input("Enter a number 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp -1] == "-":
        board[inp-1] = current_player
    else:
        print("oops the spot has been taken by other player")

# win or die
def check_horizontal(board):
    global winner 
    if board[0] == board[1] == board [2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board [5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board [8] and board[6] != "-":
        winner = board[6]
        return True

def check_row(board):
    global winner
    if board[0] == board[3] == board [6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board [7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board [8] and board[2] != "-":
        winner = board[2]
        return True

def check_diagonal(board):
    global winner
    if board[0] == board[4] == board [8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board [6] and board[2] != "-":
        winner = board[2]
        return True

def check_tie(board):
    global game_running
    if "-" not in board:
        print_board(board)
        print("It's a tie!")
        game_running = False

def check_win():
    if check_horizontal(board) or check_row(board) or check_diagonal(board):
        print(f"The winner is {winner}")

# Swith player      

def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"


# Computer
import random
def computer(board):
    while current_player == "O":
        position = random.randint(0,8)
        if board[position] == "-":
            board[position] = "O"
            switch_player()

# Rules

while game_running:
    print_board(board)
    player_input(board)
    check_win()
    check_tie(board)
    switch_player()
    computer(board)
    check_win()
    check_tie(board)




