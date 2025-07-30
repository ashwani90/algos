let a = [-2,-1,0,3,5,6,7,9,13,14];
sum = 12;
console.log(printAllPairs(a,12));

function printAllPairs(arr,sum) {
    // arr.sort();
    let first = 0;
    let last = arr.length - 1;
    let pairs = [];
    
    while (first<last) {
        let s = arr[first] + arr[last];
        
        if (s==sum) {
            first++;
            last--;
            pairs.push([first,last]);
            continue;
        }
        if (s>sum) {
            last--;
        } else {
            first++
        }
    }
    return pairs;
}