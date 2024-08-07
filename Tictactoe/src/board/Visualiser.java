package board;

public abstract class Visualizer {

    public static void printBoard(Board board) {
        System.out.println( "Board: ");
        for (int row = 0; row < board.getSize(); row++){
            System.out.println("|");
            for(int col = 0; col < board.getSize(); col++){
                System.out.println(" ");
                System.out.println((board.getPieceAt(new Position(row, col)) == null ? "     "
                        : board.getPieceAt(new Position(row, col))));
                System.out.println(" | ");
            }
            System.out.println("");
            System.out.println(new String(new char[board.getSize()]).replace("\O", "--------"));
        }
    }
}
