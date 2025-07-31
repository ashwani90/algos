console.log(makeChange(100,25));

function makeChange(n,denom) {
    let next_denom = 0;
    switch (denom) {
        case 25:
            next_denom = 10;
            break;
        case 10:
            next_denom = 5;
            break;
        case 5:
            next_denom = 1;
            break;
        case 1:
            return 1;
    }
    let ways = 0;
    for (let i=0;i*denom <= n;i++) {
        ways += makeChange(n-i*denom, next_denom);
    }
    return ways;
}