/**
 * @param {string} IP
 * @return {string}
 */
var validIPAddress = function(IP) {
    function v4(s) {
        let ss = s.split('.');
        if (ss.length !== 4) return false;
        for (let i = 0; i < 4; i++) {
            if (!/^(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]?|0)$/.test(ss[i])) {
                return false;
            }
        }
        return 'IPv4';
    }
    function v6(s) {
        let ss = s.split(':');
        if (ss.length !== 8) return false;
        for (let i = 0; i < 8; i++) {
            if (!/^[0-9a-fA-F]{1,4}$/.test(ss[i])) {
                return false;
            }
        }
        return 'IPv6';
    }
    return v4(IP) || v6(IP) || 'Neither';
};
