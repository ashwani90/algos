function shortest(words,word1,word2) {
    let pos1 = -1;
    let min = Math.max;
    let pos2 = -1;
    let distance = min;
    for (let i=0;i<words.length;i++) {
        if (words[i] == word1) {
            pos1 = i;

        }
        if (words[i] == word2) {
            pos2 = i;
            distance = pos2 - pos1;
            if (pos2>= 0 && distance<min) {
                min = distance;
            }
        }
    }
    return min;
}

// Work on suffix tree
// Work on linked list implementation of word transforming changing one character to another
// I will come back to this later on for solving hard problems