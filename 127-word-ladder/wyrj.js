/**
 * @param {string} beginWord
 * @param {string} endWord
 * @param {string[]} wordList
 * @return {number}
 */
var ladderLength = function(beginWord, endWord, wordList) {
    var isNeighbor = function(w1, w2) {
        var flag = false;
        for (var k = 0; k < w1.length; k++) {
            if (w1[k] !== w2[k]) {
                if (flag) return false;
                flag = true;
            }
        }
        return flag;
    }
    
    var len = wordList.length;
    var ans = 1, arr = [beginWord], crossIndex = 0;
    var i, j, currWord;
    for (i = 0; i < arr.length; i++) {
        if (i > crossIndex) {
            crossIndex = arr.length - 1;
            ans++;
        }
        currWord = arr[i];
        for (j = 0; j < len; j++) {
            if (isNeighbor(currWord, wordList[j])) {
                if (wordList[j] === endWord) {
                    return ans + 1;
                }
                arr.push(wordList[j]);
                wordList[j] = wordList[len - 1];
                len--;
                j--;
            }
        }
    }
    return 0;
};