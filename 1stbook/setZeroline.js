let matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,0],
];
let row = [];
let column = [];
for (let i=0;i<matrix.length;i++) {
    for (let j=0;j<matrix[i].length;j++) {
        if (matrix[i][j] == 0) {
            row.push(i);
            column.push(j);
        }
    }
}

for (let i=0;i<matrix.length;i++) {
    for (let j=0;j<matrix[i].length;j++) {
        if (row.includes(i) || row.includes(j)) {
            matrix[i][j] = 0;
        }
    }
}

console.log(matrix);