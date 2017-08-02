/**
 * @param {string} secret
 * @param {string} guess
 * @return {string}
 */
var getHint = function(secret, guess) {
    var s = {}, g = {};
    var a = 0, b = 0;
    for (var i=0;i<guess.length;++i) {
        if (secret[i] === guess[i]) ++a;
        else {
            if (!(secret[i] in s)) { s[secret[i]] = 0; }
            if (!(guess[i] in g)) { g[guess[i]] = 0; }
            ++s[secret[i]];
            ++g[guess[i]];
        }
    }
    for (var i in g) {
        if (i in s) {
            b += Math.min(s[i], g[i]);
        }
    }
    return ""+a+"A"+b+"B";
};
