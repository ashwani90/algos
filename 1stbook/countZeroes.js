n = 10;
console.log(countZeroes(n));
function countZeroes(n) {
    let count = 0;
    let iter = 0;
    for (let i=n;i>0;i--) {
        let j=i;
        while(j%5 == 0) {
            count++;
            j /= 5;
            iter++;
        }
    }
    return count;
}

