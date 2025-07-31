function rand7() {
    while(true) {
        let r1 = 2*rand5();
        let r2 = rand5();
        if (r2!=4) {
            let rand1 = r2%2;
            let num = r1 + rand1;
            if (num<7) {
                return num;
            }
        }
    }
}