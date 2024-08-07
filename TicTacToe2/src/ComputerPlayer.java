import java.util.Random;

enum Difficulty {
    easy, hard
}

public class ComputerPlayer extends Player {
    public Difficulty difficulty;

    public ComputerPlayer(Game game, Difficulty difficulty) {
        super(game);
        this.difficulty = difficulty;
    }

    public void computerTurn(char[][] board) {
        if(difficulty == Difficulty.easy)
        {
            computerTurnEasy(board);
        }else{
            computerTurnHard(board);
        }
    }

    private void computerTurnEasy(char[][] board) {

        Random rand = new Random(); //rand is an instance name of an object
        int computerMove;
        while (true) {
            computerMove = rand.nextInt(9) + 1; //random number between 1 and 9. Random is an integer, but we need char, so we need to convert it to string and back to char
            if (brain.isValidMove(board, computerMove)){
                break;
            }
        }
        System.out.println("Computer chose " + computerMove);
        placeMove(board, computerMove, 'O'); //convert the computer move to string
    }
    private void computerTurnHard(char[][] board) {
        Random rand = new Random();
        int computerMove;
        while (true) {
            // Computer try to win
            int winningPositionO = brain.possibleWin(game.board, 'O');
            int winningPositionX = brain.possibleWin(game.board, 'X');
            if (winningPositionO != 0){
                System.out.println("computer going for the win");
                computerMove = winningPositionO;
            } else if (winningPositionX != 0) {
                System.out.println("computer blocking");
                computerMove = winningPositionX;
            }else{
                System.out.println("computer random move");
                computerMove = rand.nextInt(9) + 1; //random number between 1 and 9
            }
            if (brain.isValidMove(board, computerMove)){
                break;
            }
        }
        System.out.println("Computer chose " + computerMove);
        placeMove(board, computerMove, 'O'); //convert the computer move to string
    }
}
