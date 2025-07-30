let n = 3;
let setData = [];
function generateParens(remaining,setData) {
    if (remaining == 0) {
        setData.push("");
    } else {
        let prev = generateParens(remaining-1,setData);
        for (let i=0;i<prev.length;i++) {
            for (let j=0;j<prev[i].length;j++) {
                if (prev[i].charAt(j) == '(') {
                    let s = insertInside(prev[i], j);
                    setData.push(s);
                }
            }
            if (!setData.includes("()"+prev[i])) {
                setData.push("()" + prev[i]);
            }
        }
    }

}

function insertInside(str,leftIndex) {
    let left = str.slice(0,leftIndex+1);
    let right = str.slice(leftIndex+1,str.length);
    return left+"()"+right;
}