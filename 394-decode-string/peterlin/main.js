/**
 * @param {string} s
 * @return {string}
 */
var decodeString = function(s) {
    console.log(s.match(/^\d+/));
    var st = [];
    var ss = [""];
    while (s.length > 0) {
        var k = s.match(/^\d+/);
        if (k !== null) {
            st.push(parseInt(k[0]));
            ss.push("");
            s = s.slice(k[0].length+1);
            continue;
        }
        if (s[0] === "]") {
            var top = ss.pop();
            ss[ss.length-1] += top.repeat(st.pop());
            s = s.slice(1);
            continue;
        }
        ss[ss.length-1] += s[0];
        s = s.slice(1);
    }
    return ss[0];
};
