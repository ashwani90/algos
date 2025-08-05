const st = "aabcdsdwdacdshahdkaklsjfkteqwej";
console.log(longestSubstring(st));
function longestSubstring(s) {
    let lastIndex = new Array(256).fill(-1);
    console.log(lastIndex);
    let i =0, res=0;
    for (let j=0;j<s.length;j++) {
        i = Math.max(i, lastIndex[s.charAt(j)] + 1);
        res = Math.max(res, j - i + 1);
        lastIndex[s.charAt(j)] = j;
    }
    return res;
}