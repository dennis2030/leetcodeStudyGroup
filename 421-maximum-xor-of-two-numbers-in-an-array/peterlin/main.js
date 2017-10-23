/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaximumXOR = function(nums) {
    var node = function() {
        this.zero = this.one = null;
    }
    
    var root = new node();
    nums.forEach(x => {
        var b = 1 << 30;
        var c = root;
        for (var b = 1 << 30; b > 0; b >>= 1) {
            if (x & b) {
                if (c.one === null) c.one = new node();
                c = c.one;
            } else {
                if (c.zero === null) c.zero = new node();
                c = c.zero;
            }
        }
    });
    var ans = 0;
    nums.forEach(x => {
        var b = 1 << 30;
        var c = root;
        var d = 0;
        for (var b = 1 << 30; b > 0; b >>= 1) {
            if (x & b) {
                if (c.zero !== null) {
                    d += b;
                    c = c.zero;
                } else {
                    c = c.one;
                }
            } else {
                if (c.one !== null) {
                    d += b;
                    c = c.one;
                } else {
                    c = c.zero;
                }
            }
            ans = Math.max(ans, d);
        }
    });
    return ans;
};
