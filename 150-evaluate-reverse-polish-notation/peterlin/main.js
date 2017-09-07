/**
 * @param {string[]} tokens
 * @return {number}
 */
var evalRPN = function(tokens) {
    var s = [];
    tokens.forEach(x => {
        if (x === "+") {
            s.push(s.pop()+s.pop());
        } else if (x === "-") {
            s.push(-(s.pop()-s.pop()));
        } else if (x === "*") {
            s.push(s.pop()*s.pop());
        } else if (x === "/") {
            s.push(parseInt(1/(s.pop()/s.pop())));
        } else {
            s.push(parseInt(x));
        }
    });
    return s[0];
};
