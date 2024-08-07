import java.util.Scanner;

import static java.lang.Integer.parseInt;

public class Player {

    public Game game;
    public BoardValidator brain;
    public Player(Game game) {
        this.game = game;
        this.brain = new BoardValidator();
    }

    public void playerTurn(char[][] board, Scanner scanner)
    {
        int userInput;
        while (true)
        {
            System.out.println("Which place you would like to take ? Input number 1-9.");
            userInput = parseInt(scanner.nextLine());
            if (brain.isValidMove(board, userInput)) { // convert String to char example : String s="hello"; char c=s.charAt(0);//returns h
                placeMove(game.board.cells, userInput, 'X');
                break;
            } else {
                System.out.println(userInput + " is not a valid move.");
            }
        }
    }

    public void placeMove(char[][] board, int position, char symbol) {
        switch(position) {
            case 1:
                board[0][0] = symbol;
                break;
            case 2:
                board[0][1] = symbol;
                break;
            case 3:
                board[0][2] = symbol;
                break;
            case 4:
                board[1][0] = symbol;
                break;
            case 5:
                board[1][1] = symbol;
                break;
            case 6:
                board[1][2] = symbol;
                break;
            case 7:
                board[2][0] = symbol;
                break;
            case 8:
                board[2][1] = symbol;
                break;
            case 9:
                board[2][2] = symbol;
                break;
            default:
                System.out.println(":(");
        }
    }
}
