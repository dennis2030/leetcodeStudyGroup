/**
 * @param {string[]} dict
 * @param {string} sentence
 * @return {string}
 */
var replaceWords = function(dict, sentence) {
    dict.sort();
    let s = sentence.split(' ');
    for (let i = 0; i < s.length; i++) {
        for (let j = 0; j < dict.length; j++) {
            if (s[i].startsWith(dict[j])) {
                s[i] = dict[j];
                break;
            }
        }
    }
    return s.join(' ');
};
