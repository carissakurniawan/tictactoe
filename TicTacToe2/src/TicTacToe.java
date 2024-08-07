import java.util.Scanner;

public class TicTacToe {
    static Game game = new Game();
    static Difficulty difficulty = Difficulty.easy;
    static ComputerPlayer computerPlayer;
    static Player player = new Player(game);

    public static void main(String[] args) {

        //Declare scanner
        Scanner scanner = new Scanner(System.in);

        //Select level
        difficulty = game.selectDifficulty(scanner);

        //Assigning the level
        computerPlayer = new ComputerPlayer(game, difficulty);
        System.out.println(difficulty);

        // To make it keep playing until someone win
        while (true) {
            //Human player takes turn
            player.playerTurn(game.board.cells, scanner);
            if (game.isGameFinished()){
                System.out.println( player + "wins!");
                break;
            }
            game.board.printBoard();

            //Computer move
            computerPlayer.computerTurn(game.board.cells);
            if (game.isGameFinished()) {
                break;
            }
            game.board.printBoard();
        }
        scanner.close();
    }
}

