/**
 * @param {string} IP
 * @return {string}
 */
var validIPAddress = function(IP) {
    if (/^([1-9]\d{0,2}|0)(?:\.([1-9]\d{0,2}|0)){3}$/.test(IP)) {
        if (IP.split(".").every(n => parseInt(n) < 256)) return "IPv4";
    }
    if (/^([0-9a-fA-F]{1,4})(\:[0-9a-fA-F]{1,4}){7}$/.test(IP)) return "IPv6";
    return "Neither";
};
