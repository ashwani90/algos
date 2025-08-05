function maxProduct(A) {
    if (A.length <= 0) return;
    let max = A[0], min = A[0], maxAns = A[0];
    for (let i=0;i<A.length;i++) {
        let mx=max, mn=min;
        max = Math.max(Math.max(A[i], mx*A[i]), mn*A[i]);
        min = Math.min(Math.min(A[i], mx*A[i]), mn*A[i]);
        maxAns = Math.max(max,maxAns);
    }
    return maxAns;
}

// Need to keep track of both min and max