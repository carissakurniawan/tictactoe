import board.Visualiser;
import player.ComputerPlayer;
import player.HumanPlayer;

public class Main {
    public static void main(String[] args) throws TileNotOnBoardException {
        Board board = new Board(3);
        Visualiser.printBoard(startBoard);
        HumanPlayer humanPlayer = new HumanPlayer();

        Position position = humanPlayer.chooseAMove();
        board = board.placePieceAt(position, new XPiece());

        Position position1 = new ComputerPlayer().chooseAMove(board);
        Visualiser.printBoard(board.placePieceAt(position1, XPiece()));
    }
}