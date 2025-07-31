let matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
];

// output should be like [[3,6,9],[2,5,8],[1,4,7]]
n=3;
for (let layer = 0;layer<n/2;++layer) {
    let first = layer;
    let last = n-1-layer;
    for (let i=first;i<last;++i) {
        let offset = i-first;
        let top = matrix[first][i];
        matrix[first][i] = matrix[last-offset][first];
        matrix[last-offset][first] = matrix[last][last-offset];
        matrix[last][last-offset] = matrix[i][last];
        matrix[i][last] = top;
    }
}

console.log(matrix);