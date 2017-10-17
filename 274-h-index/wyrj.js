/**
 * @param {number[]} citations
 * @return {number}
 */
var hIndex = function(citations) {
    citations.sort((l, r) => r - l);
    for (let i = 0; i < citations.length; i++) {
        if (citations[i] < i + 1) return i;
    }
    return citations.length;
};
