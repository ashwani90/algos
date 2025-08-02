let a = [1,2,3,4,5,10,8,7,12,13,14,15];

const findEndofLeftSubsequence = (arr) => {
    for (let i=0;i<arr.length-1;i++) {
        if (arr[i]> arr[i+1]) {
            return i;
        }
    }
    return arr.length-1;
}
const findStartofRightSubsequence = (arr) => {
    for (let i=arr.length-2;i>0;i--) {
        if (arr[i] > arr[i+1]) {
            return i+1;
        }
    }
    return 0;
}
const shrinkLeft = (arr,min_index,start) => {
    let comp = arr[min_index];
    for (let i=start-1;i>=0;i--) {
        if (arr[i]<=comp) {
            return i+1;
        }
        return 0;
    }
}
const shrinkRight = (arr,max_index,start) => {
    let comp = arr[max_index];
    for (let i=start;i<arr.length;i++) {
        if (arr[i] >= comp) {
            return i-1;
        }
        return arr.length - 1;
    }
}
const findUnsortedSequence = (arr) => {
    let end_left = findEndofLeftSubsequence(arr);
    let start_right = findStartofRightSubsequence(arr);
    let min_index = end_left + 1;
    if (min_index >= arr.length) {
        return;
    }
    let max_index = start_right - 1;
    for (let i=end_left;i<=start_right;i++) {
        if (arr[i] < arr[min_index]) {
            min_index = i;
        }
        if (arr[i] > arr[max_index]) {
            max_index = i;
        }
    }
    let left_index = shrinkLeft(arr,min_index,end_left);
    let right_index = shrinkRight(arr,max_index,start_right);

    console.log(left_index + " " + right_index);
}

findUnsortedSequence(a);