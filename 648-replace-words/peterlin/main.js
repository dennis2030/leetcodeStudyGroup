/**
 * @param {string[]} dict
 * @param {string} sentence
 * @return {string}
 */
var replaceWords = function(dict, sentence) {
    return sentence.split(' ').map(c => {
        return dict.reduce((w, d) => {
            return w.length > d.length && w.slice(0, d.length) === d ? d : w;
        }, c);
    }).join(' ');
};
