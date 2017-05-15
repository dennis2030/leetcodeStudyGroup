/**
 * @param {string} preorder
 * @return {boolean}
 */
var isValidSerialization = function(preorder) {
    let arr = preorder.split(',');
    let ans = true;
    let stack = [];
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] !== '#') stack.push(arr[i]);
        else {
            while (true) {
                if (stack.length === 0 && i !== arr.length - 1) return false;
                else if (stack[stack.length - 1] === '#') {
                    stack.length -= 2;
                } else {
                    stack.push('#');
                    break;
                }
            }
        }
    }
    return stack.length === 1 && stack[0] === '#';
};