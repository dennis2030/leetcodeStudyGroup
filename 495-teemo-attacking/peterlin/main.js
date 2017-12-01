/**
 * @param {number[]} timeSeries
 * @param {number} duration
 * @return {number}
 */
var findPoisonedDuration = function(timeSeries, duration) {
    return timeSeries.reduceRight((tot, cur, i) => {
        return i === timeSeries.length-1 ? duration : tot+Math.min(duration, timeSeries[i+1]-cur);
    }, 0);
};
