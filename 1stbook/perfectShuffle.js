// Simple random function
function rand(lower, higher) {
    return lower + (Math.random() * (higher-lower+1));
}

function shuffleArrayRecursively(cards,i) {
    if (i==0) {
        return cards;
    }

    shuffleArrayRecursively(cards,i-1);
    let k = rand(0,i);
    let temp = cards[k];
    cards[k] = cards[i];
    cards[i] = temp;
    return cards;
}