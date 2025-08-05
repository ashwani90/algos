function maxSubArray(A) {
    let maxEnd=A[0];
    for (let i=0;i<A.length;i++) {
        let maxEndHere = Math.max(maxEnd+A[i], A[i]);
        maxEnd = Math.max(maxEndHere,maxEnd);
    }
    return maxEnd;
}