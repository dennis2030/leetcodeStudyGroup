/**
 * @param {character[]} tasks
 * @param {number} n
 * @return {number}
 */
var leastInterval = function(tasks, n) {
    let map = {};
    for (let i = 0; i < tasks.length; i++) {
        if (!map[tasks[i]]) map[tasks[i]] = 0;
        map[tasks[i]] += 1;
    }
    let max = 0;
    let maxCount = 0;
    for (let name in map) {
        if (map[name] === max) {
            maxCount += 1;
        } else if (map[name] > max) {
            max = map[name];
            maxCount = 1;
        }
    }
    return Math.max((max - 1) * (n + 1) + maxCount, tasks.length);
};
