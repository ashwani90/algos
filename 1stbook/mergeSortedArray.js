let a = [1,4,6,8,10];
let b = [5,7,9,11];
let result = [];
let j = 0;
for (let i =0;i<a.length;i++) {
    if (j<b.length) {
        while (a[i]>b[j] ) {
            result.push(b[j]);
            j++;
        } 
    } 
    result.push(a[i]);
}
while(j<b.length) {
    result.push(b[j]);
        j++;
}

console.log(result);