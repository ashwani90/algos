let arr = [];
let q3 = [3];
let q5 = [5];
let q7 = [7];
let k =10;
arr.push(1);
let itemNo = 0;
let result = 0;
while (itemNo<k) {
    let x = getMinfromArrays(q3,q5,q7);
    arr.push(x);
    if (q3.includes(x)) {
        q3.push(x*3);
        q5.push(x*5);
        q7.push(x*7);
        removeItem(q3,x);
    }
    if (q5.includes(x)) {
        q5.push(x*5);
        q7.push(x*7);
        removeItem(q5,x);
    }
    if (q7.includes(x)) {
        q7.push(x*7);
        removeItem(q7,x);
    }
    result = x;
    itemNo++;
}
console.log(result);
function getMinfromArrays(q3,q5,q7) {
    Array.prototype.min = function() {
        return Math.min.apply(null, this);
      };
      let q3min = q3.min();
      let q5min = q5.min();
      let q7min = q7.min();
      return Math.min(q3min,q5min,q7min);
}

function removeItem(arr,x) {
    const index = arr.indexOf(x);
    if (index > -1) { // only splice array when item is found
        arr.splice(index, 1); // 2nd parameter means remove one item only
    }
    return arr;
}