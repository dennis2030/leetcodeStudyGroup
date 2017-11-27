/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaximumXOR = function(nums) {
    let max = 0, mask = 0;
    for (let i = 31; i >= 0; i--) {
        let s = new Set();
        mask = mask | (1 << i);
        nums.forEach((n) => {
            s.add(n & mask);
        });
        
        let temp = max | (1 << i);
        s.forEach((n) => {
            if (s.has(n ^ temp)) {
                max = temp;
                return false;
            }
        });
    }
    return max;
};
