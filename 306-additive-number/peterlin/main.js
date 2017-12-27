/**
 * @param {string} num
 * @return {boolean}
 */
var isAdditiveNumber = function(num) {
    const check = (a, b) => {
        let n1 = parseInt(num.slice(0, a));
        let n2 = parseInt(num.slice(a, b));
        
        if (n1.toString() != num.slice(0, a)) return false;
        if (n2.toString() != num.slice(a, b)) return false;
        
        let st = b;
        for (let st=b;st<num.length;n2+=n1, n1=n2-n1) {
            const ns = (n1+n2).toString();
            if (!num.slice(st).startsWith(ns)) return false;
            st += ns.length;
        }
        return true;
    };
    
    for (let i=1;i<num.length/2;++i) {
        for (let j=i+1;j<num.length;++j) {
            if (check(i, j)) return true;
        }
    }
    return false;
};
