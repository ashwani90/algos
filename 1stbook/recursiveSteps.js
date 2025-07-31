

// function countWays(n) {
//     if (n<0) {
//         return 0;
//     } else if (n==0) {
//         return 1;
//     } else {
//         return countWays(n-1) + countWays(n-2) + countWays(n-3);
//     }
// }
let map = {};
console.log(countWays(11, map));
// optimized version
function countWays(n,map) {
    if (n<0) {
        return 0;
    } else if (n==0) {
        return 1;
    } else if (map[n]) {
        return map[n];
    } 
    else {
        map[n] = countWays(n-1,map) + countWays(n-2,map) + countWays(n-3,map);
        return map[n];
    }
}