let arr = [2,3,-8,-1,2,4,-2,3];

console.log(getMaxSum(arr));

function getMaxSum(arr) {
    let maxSum = 0;
    let sum =0;
    for (let i=0;i<arr.length;i++) {
        sum += arr[i];
        if (maxSum<sum) {
            maxSum = sum;
        } else if (sum<0) {
            sum = 0;
        }
    }
    return maxSum;
}