import java.util.Scanner;

import static java.lang.Integer.parseInt;

public class Game {
    public Board board = new Board();
    public Game() {
    }

    public Difficulty selectDifficulty(Scanner scanner) {
        int userInput;
        System.out.println("Welcome to TicTacToe! What difficulty level you would like to play ? Press 1 for easy and 2 for hard");
        while (true) {
            userInput = parseInt(scanner.nextLine());
            System.out.println(userInput);
            if (isValidDifficulty(userInput))
            {
                if (userInput == 1) {
                    return Difficulty.easy;
                }
                else {
                    return Difficulty.hard;
                }
            }
            System.out.println("Invalid move! You must input 1 or 2.");
        }
    }

    public boolean isGameFinished() {
        if (playerWon(board.cells, 'X')) {
            board.printBoard();
            System.out.println("Human player wins");
            return true;
        }
        if (playerWon(board.cells, 'O')) {
            board.printBoard();
            System.out.println("Computer wins");
            return true;
        }

        for (int i = 0; i < board.cells.length; i++) {
            for (int j = 0; j < board.cells[i].length; j++) {
                if (board.cells[i][j] == ' ') { //if there is still a blank spot, the game is not finished yet.
                    return false; //so return false
                }
            }
        }
        board.printBoard();
        System.out.println("It's a tie!");
        return true;
    }

    public boolean isValidDifficulty(int position) {
        switch (position) {
            case 1:
            case 2:
                return true;
            default:
                return false;
        }
    }

    public static boolean playerWon(char[][] board, char symbol) {
        if ((board[0][0] == symbol && board[0][1] == symbol && board[0][2] == symbol) ||
                (board[1][0] == symbol && board[1][1] == symbol && board[1][2] == symbol) ||
                (board[2][0] == symbol && board[2][1] == symbol && board[2][2] == symbol) ||

                (board[0][0] == symbol && board[1][1] == symbol && board[2][0] == symbol) ||
                (board[0][1] == symbol && board[1][1] == symbol && board[2][1] == symbol) ||
                (board[0][2] == symbol && board[1][2] == symbol && board[2][2] == symbol) ||

                (board[0][0] == symbol && board[1][1] == symbol && board[2][2] == symbol) ||
                (board[0][1] == symbol && board[1][1] == symbol && board[2][1] == symbol)) {
            return true;
        } //we dont need an else because if we met the statement above, it will be true, and the others are false
        return false;
    }
}
