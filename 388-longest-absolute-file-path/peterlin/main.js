/**
 * @param {string} input
 * @return {number}
 */
var lengthLongestPath = function(input) {
    var s = [], x = 0, length = 0;
    input.split('\n').forEach(line => {
        var names = line.split('\t');
        var name = names[names.length-1];
        while (s.length >= names.length) { length -= s.pop(); }
        if (name.includes('.')) {
            x = Math.max(x, name.length+length);
        } else {
            length += name.length+1;
            s.push(name.length+1);
        }
    });
    return x;
};
