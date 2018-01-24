/**
 * @param {string} input
 * @return {number[]}
 */
var diffWaysToCompute = function(input) {
    let r = (op, nums) => {
        if (nums.length === 1) {
            return nums;
        }
        const arr = [];
        for (let i = 0; i < op.length; i++) {
            const pre = r(op.slice(0, i), nums.slice(0, i + 1));
            const post = r(op.slice(i + 1), nums.slice(i + 1));
            let value;
            for (let j = 0; j < pre.length; j++) {
                for (let k = 0; k < post.length; k++) {
                    if (op[i] === '+') value = pre[j] + post[k];
                    else if (op[i] === '-') value = pre[j] - post[k];
                    else if (op[i] === '*') value = pre[j] * post[k];
                    arr.push(value);
                }
            }
        }
        return arr;
    }
    return r(input.split(/\d+/).slice(1, -1), input.split(/[\+\-\*]/).map((n) => parseInt(n, 10)));
};
