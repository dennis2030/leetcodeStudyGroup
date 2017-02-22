/**
 * @param {string} beginWord
 * @param {string} endWord
 * @param {string[]} wordList
 * @return {number}
 */
var ladderLength = function(beginWord, endWord, wordList) {
    var dist = {};
    for (var index in wordList) {
        dist[wordList[index]] = 0;
    }
    dist[beginWord] = 1;
    
    var queue = [beginWord];
    while (queue.length > 0) {
        var word = queue.shift();
        for (var i=0;i<word.length;++i) {
            for (var j="a".charCodeAt(0);j<="z".charCodeAt(0);++j) {
                var newWord = word.substr(0, i) + String.fromCharCode(j) + word.substr(i+1);
                if (dist[newWord] === 0) {
                    dist[newWord] = dist[word]+1;
                    queue.push(newWord);
                }
            }
        }
        if (dist[endWord] > 0) break;
    }
    return dist[endWord] || 0;
};
