function findElement(matrix, k) {
    let row = 0;
    let col = matrix[0].length-1;
    while (row<matrix.length && col >=0 ) {
        if (matrix[row][col] == k) {
            return true;
        } else if (matrix[row][col] > elem) {
            col--;
        } else {
            row++;
        }
    }
}