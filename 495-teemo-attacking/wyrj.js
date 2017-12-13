/**
 * @param {number[]} timeSeries
 * @param {number} duration
 * @return {number}
 */
var findPoisonedDuration = function(timeSeries, duration) {
    let ans = timeSeries.length > 0 ? duration : 0;
    for (let i = 1; i < timeSeries.length; i++) {
        const diff = timeSeries[i] - timeSeries[i - 1];
        ans += Math.min(diff, duration);
    }
    return ans;
};
