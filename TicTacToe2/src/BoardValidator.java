public class BoardValidator {

    public int possibleWin(Board board, int symbol) {
        char cell1 = getCell(board.cells,  1);
        char cell2 = getCell(board.cells, 2);
        char cell3 = getCell(board.cells, 3);
        char cell4 = getCell(board.cells, 4);
        char cell5 = getCell(board.cells, 5);
        char cell6 = getCell(board.cells, 6);
        char cell7 = getCell(board.cells, 7);
        char cell8 = getCell(board.cells, 8);
        char cell9 = getCell(board.cells, 9);

        if (cell1 == ' ' && cell2 == symbol && cell3 == symbol)
            return 1;
        if (cell1 == symbol && cell2 == ' ' && cell3 == symbol)
            return 2;
        if (cell1 == symbol && cell2 == symbol && cell3 == ' ')
            return 3;
        if (cell4 == ' ' && cell5 == symbol && cell6 == symbol)
            return 4;
        if (cell4 == symbol && cell5 == ' ' && cell6 == symbol)
            return 5;
        if (cell4 == symbol && cell5 == symbol && cell6 == ' ')
            return 6;
        if (cell7 == ' ' && cell8 == symbol && cell9 == symbol)
            return 7;
        if (cell7 == symbol && cell8 == ' ' && cell9 == symbol)
            return 8;
        if (cell7 == symbol && cell8 == symbol && cell9 == ' ')
            return 9;
        if (cell1 == ' ' && cell4 == symbol && cell7 == symbol)
            return 1;
        if (cell1 == symbol && cell4 == ' ' && cell7 == symbol)
            return 4;
        if (cell1 == symbol && cell4 == symbol && cell7 == ' ')
            return 7;
        if (cell2 == ' ' && cell5 == symbol && cell8 == symbol)
            return 2;
        if (cell2 == symbol && cell5 == ' ' && cell8 == symbol)
            return 5;
        if (cell2 == symbol && cell5 == symbol && cell8 == ' ')
            return 8;
        if (cell3 == ' ' && cell6 == symbol && cell9 == symbol)
            return '3';
        if (cell3 == symbol && cell6 == ' ' && cell9 == symbol)
            return 6;
        if (cell3 == symbol && cell6 == symbol && cell9 == ' ')
            return 9;
        if (cell1 == ' ' && cell5 == symbol && cell9 == symbol)
            return 1;
        if (cell1 == symbol && cell5 == ' ' && cell9 == symbol)
            return 5;
        if (cell1 == symbol && cell5 == symbol && cell9 == ' ')
            return 9;
        if (cell3 == ' ' && cell5 == symbol && cell7 == symbol)
            return 3;
        if (cell3 == symbol && cell5 == ' ' && cell7 == symbol)
            return 5;
        if (cell3 == symbol && cell5 == symbol && cell7 == ' ')
            return 7;
        return 0;
    }

    public boolean possibleCorner(Board board) {
        if (
                isValidMove(board.cells, 1)
                        || isValidMove(board.cells, 3)
                        || isValidMove(board.cells, 7)
                        || isValidMove(board.cells, 9)
        ) {
            return true;
        }
        return false;
    }

    public boolean possibleSide(Board board) {
        if (
                isValidMove(board.cells, 4)
                        || isValidMove(board.cells, 6)
                        || isValidMove(board.cells, 2)
                        || isValidMove(board.cells, 8)
        ) {
            return true;
        }
        return false;
    }

    public boolean possibleMiddle(Board board){
        return isValidMove(board.cells, 5);
    }

    public char getCell(char[][] cells, int position){
        switch (position) {
            case 1:
                return cells[0][0];
            case 2:
                return cells[0][1];
            case 3:
                return cells[0][2];
            case 4:
                return cells[1][0];
            case 5:
                return cells[1][1];
            case 6:
                return cells[1][2];
            case 7:
                return cells[2][0];
            case 8:
                return cells[2][1];
            case 9:
                return cells[2][2];
            default:
                return 0;
        }
    }
    public boolean isValidMove(char[][] boardCells, int position) {
        switch (position) {
            case 1:
                return (boardCells[0][0] == ' ');
            case 2:
                return (boardCells[0][1] == ' ');
            case 3:
                return (boardCells[0][2] == ' ');
            case 4:
                return (boardCells[1][0] == ' ');
            case 5:
                return (boardCells[1][1] == ' ');
            case 6:
                return (boardCells[1][2] == ' ');
            case 7:
                return (boardCells[2][0] == ' ');
            case 8:
                return (boardCells[2][1] == ' ');
            case 9:
                return (boardCells[2][2] == ' ');
            default:
                return false;
        }
    }
}
