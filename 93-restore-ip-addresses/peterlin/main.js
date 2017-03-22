/**
 * @param {string} s
 * @return {string[]}
 */
var restoreIpAddresses = function(s) {
    var i,j,k,len=s.length,a=[];
    for (i=1;i<Math.min(4, len);++i)
        for (j=i+1;j<Math.min(i+4, len);++j)
            for (k=j+1;k<Math.min(j+4, len);++k) {
                var ok = true;
                var b = [s.substring(0,i), s.substring(i,j), s.substring(j,k), s.substring(k)];
                b.forEach((n) => {  
                    if (n[0] === "0" && n.length > 1) ok = false;
                    else if (parseInt(n) > 255) ok = false;
                });
                if (ok) a.push(b.join("."));
            }
    return a;
};
