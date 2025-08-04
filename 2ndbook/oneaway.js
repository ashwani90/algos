function oneEditAway(first,second) {
    if (first.length == second.length) {
        return oneEditReplace(first,second);
    } else if (first.length+1 == second.length) {
        return oneEditInsert(first,second);
    } else if (first.length == second.length+1) {
        return oneEditInsert(second,first);
    }
    // It means not one insert away
    return false;
}

function oneEditReplace(first,second) {
    let foundDifference = false;
    for (let i=0; i<second.length;i++) {
        if (first[i]!=second[i]) {
            if (foundDifference) {
                return false;
            }
            foundDifference = true;
        }
    }
    return true;
}

function oneEditInsert(first,second) {
    let index1 = 0;
    let index2 = 0;
    while(index2 < second.length && index1 < first.length) {
        if (first[index1] != second[index2]) {
            if (index1 != index2) {
                return false;
            }
            index2++;
        } else {
            index1++;
            index2++;
        }
       
    } 
    return true;
}
