function parseSimple(wordStart,wordEnd) {
    if (wordEnd >= sentence.length()) {
        return wordEnd - wordStart;
    }

    word = sentence.slice(wordStart, wordEnd+1);

    let bestExact = parseSimple(wordEnd+1, wordEnd+1);
    if (!dictinoary.contains(word)) {
        bestExact += word.length();
    }

    let baseExtend = parseSimple(wordStart, wordEnd+1);
    return Math.min(bestExact, baseExtend);
}