function numberOf2sInRange(n) {
    let count = 0;
    for (let i=0;i<=n;i++) {
        count += numberOf2s(i);
    }
    return count;
}

function numberOf2s(n) {
    let count = 0;
    while(n>0) {
        if (n%10 == 2) {
            count++;
        }
        n= n/10;
    }
    return count;
}