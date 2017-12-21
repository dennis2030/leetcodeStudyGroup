/**
 * @param {string} input
 * @return {number[]}
 */
var diffWaysToCompute = function(input) {
    let s = input.split(/(\d+)/);
    s = s.slice(1, s.length-1);
    
    const f = (st, ed) => {
        if (st+1 == ed) {
            return [parseInt(s[st])];
        }
        let res = [];
        for (let i=st+1;i<ed;i+=2) {
            const lt = f(st, i);
            const rt = f(i+1, ed);
            res = res.concat(...lt.map(lx => rt.map(rx => s[i] == '+' ? lx+rx : s[i] == '-' ? lx-rx : lx*rx)));
        }
        return res;
    };
    return f(0, s.length);
};
