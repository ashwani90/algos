const letstr = "abcdefgh";
let permutations = [""];
console.log(getPerms(letstr,permutations));
function insertCharAt(word, c, i) {
    let start = word.slice(0,i);
    let end = word.slice(i);
    console.log(start+c+end);
    return start+c+end;
}
function getPerms(sampleStr,permutations) {
    if (sampleStr.length == 0) {
        return false;
    }
    let first = sampleStr[0];
    let remaining = sampleStr.slice(1);
    
    let words = getPerms(remaining,permutations);
    let wordLength = 0;
    if (words) {
        wordLength = words.length;
    }
    for (let i=0;i<wordLength;i++) {
        for (let j=0;j<=words[i].length;j++) {
            let s = insertCharAt(words[i],first,j);
            permutations.push(s);
        }
    }
    return permutations;
}

