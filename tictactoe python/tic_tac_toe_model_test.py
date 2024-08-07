# Your tests here

#unit test

#https://github.com/neiljp/TDD-unittest-TicTacToe/blob/master/test.py
#https://docs.python.org/3/library/unittest.html

import os
import unittest
#from unittest.mock import patch
#from io import StringIO
from tic_tac_toe_model import TicTacToe
from tic_tac_toe_move_exception import InvalidKeyException, InvalidMoveException

class TestGame(unittest.TestCase): #TestGame is a child we build from parent class unittest TestCase so we can use the build in function from TestCase

    def setUp(self):
        self.tictactoe = TicTacToe()

    # Check is winner
    def test_check_is_winner(self):

        # Check horizontal
        #given
        game = TicTacToe()

        #when
        game.update_turn('1') #X
        game.update_turn('4') #O
        game.update_turn('2') #X
        game.update_turn('5') #O
        game.update_turn('3') #X

        #then
        self.assertTrue(game.is_winner() == True)

        # Check diagonal 1
        game = TicTacToe()

        #when
        game.update_turn('1') #X
        game.update_turn('4') #O
        game.update_turn('5') #X
        game.update_turn('2') #O
        game.update_turn('9') #X

        #then
        self.assertTrue(game.is_winner() == True)


        # Check diagonal 2
        game = TicTacToe()

        #when
        game.update_turn('3') #X
        game.update_turn('4') #O
        game.update_turn('5') #X
        game.update_turn('2') #O
        game.update_turn('7') #X

        #then
        self.assertTrue(game.is_winner() == True)

        # Check vertical
        game = TicTacToe()

        #when
        game.update_turn('2') #X
        game.update_turn('1') #O
        game.update_turn('5') #X
        game.update_turn('3') #O
        game.update_turn('8') #X

        #then
        self.assertTrue(game.is_winner() == True)

    # Check valid_move
    def test_check_valid_move(self):
        
        #given
        game = TicTacToe()

        #when
        game.update_turn('5') #first turn

        #then
        self.assertFalse(game.valid_move('5')) #assert false if next turn trying to pick the same spot. Value is True because it's true that the spot is False (AssertFalse)
        self.assertTrue(game.valid_move('8')) #assert true if next turn trying to pick different spot. 
        # Assert like print those specific value. value
        
        # with self.assertRaises(InvalidKeyException): #this is still error
        #     game.valid_move('10')

    # Check update turn

    def test_check_update_turn(self):

        game = TicTacToe()

        #given
        self.assertTrue(game._current_player == 'X') # confirm first player is X

        #when update turn called
        game.update_turn('5') 

        #then next player should be updated to O
        self.assertTrue(game._current_player == 'O')


if __name__ == "__main__":
     unittest.main()







































































