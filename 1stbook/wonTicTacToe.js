function isWon(board) {
    let sum = 0;
    let factor = 1;
    for (let i=0;i<board.length;i++) {
        for (let j=0;j<board[i].length;i++) {
            let v=0;
            if (board[i][j] == "x") {
                v = 1;
            } else if (board[i][j] == 'o') {
                v = 2;
            }
            sum += v*factor;
            factor *= 3;
        }
    }
    return sum;
}