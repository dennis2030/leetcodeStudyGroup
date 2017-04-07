/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */
const STATE = {
    CHECKING: 1,
    CHECKED: 2
};
var canFinish = function(numCourses, prerequisites) {
    let record = new Array(numCourses);
    let path = new Array(numCourses);
    function checkCycle(n) {
        if (record[n] === STATE.CHECKED) return true;
        if (record[n] === STATE.CHECKING) return false;
        record[n] = STATE.CHECKING;
        for (let next in path[n]) {
            if (!path[n].hasOwnProperty(next) || !checkCycle(next)) {
                return false;
            }
        }
        record[n] = STATE.CHECKED;
        return true;
    }
    for (let i = 0; i < numCourses; i++) {
        path[i] = {};
    }
    prerequisites.forEach((prereq) => {
        path[prereq[1]][prereq[0]] = true;
    });
    for (let i = 0; i < numCourses; i++) {
        if (!checkCycle(i)) return false;
    }
    return true;
};