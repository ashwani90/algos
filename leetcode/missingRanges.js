function findMissing(vals,start,end) {
    let ranges = [];
    let prev = start-1;
    end = 0;
    for (let i=1;i<vals.length;i++) {
        curr = (i==vals.length) ? end+1 : vals[i];
        if (curr-prev >= 2) {
            end = curr-1;
            if (!vals.includes(end)) {
                if (end == prev+1) {
                    ranges.push([end]);
                } else {
                    ranges.push([prev+1,end]);
                }
            }
            
            
        }
        prev = curr;
    }
    return ranges;
}

let start = 1;
let end = 100;
let vals = [1,2,3,5,6,72,79,90];

console.log(findMissing(vals,start,end));