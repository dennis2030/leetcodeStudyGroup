/**
 * @param {number[]} citations
 * @return {number}
 */
var hIndex = function(citations) {
    var h = 0;
    citations.sort((a, b) => { return a<b?1:-1; });
    for(var i=0; i<citations.length; ++i) {
        h = Math.max(h, Math.min(citations[i], i+1));
    }
    return h;
};
