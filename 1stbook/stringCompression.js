// let abcd = "aabbcccccdddddeefffff";
let abcd = "abccdeef";
let lastChar = "";
let result = "";
currentCount = "1";
for (let i=0;i<abcd.length;i++) {
    if (lastChar == abcd[i]) {
        currentCount++;
    } else {
        if (lastChar != "") {
            if (currentCount == 1) {
                result = result + lastChar;
            } else {
                result = result + lastChar + currentCount;
            }
            
        }
        currentCount=1;
    }
    lastChar = abcd[i];
    
}
if (currentCount == 1) {
    result = result + lastChar;
} else {
    result = result + lastChar + currentCount;
}
console.log(result);
if (result.length > abcd.length) {
    console.log(abcd);
} else {
    console.log(result);
}
