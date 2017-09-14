/**
 * @param {string[]} tokens
 * @return {number}
 */
var evalRPN = function(tokens) {
    let q = [], t;
    tokens.forEach((t) => {
        switch (t) {
            case '+':
                t = q.pop();
                t = q.pop() + t;
                q.push(t);
                break;
            case '-':
                t = q.pop();
                t = q.pop() - t;
                q.push(t);
                break;
            case '*':
                t = q.pop();
                t = q.pop() * t;
                q.push(t);
                break;
            case '/':
                t = q.pop();
                t = q.pop() / t;
                q.push(~~t);
                break;
            default:
                q.push(parseInt(t));
        }
    });
    return q[0];
};
