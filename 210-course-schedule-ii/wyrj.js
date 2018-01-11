/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {number[]}
 */
var findOrder = function(numCourses, prerequisites) {
    let ans = [];
    let p = prerequisites.slice();
    let count = new Array(numCourses).fill(1);
    while (ans.length < numCourses) {
        let fail = true;
        count = count.map((c) => (c > 0) ? 0 : -1);
        let remain = [];
        for (let i = 0; i < p.length; i++) {
            count[p[i][0]] += 1;
        }
        for (let i = 0; i < numCourses; i++) {
            if (count[i] === 0) {
                ans.push(i);
                fail = false;
            }
        }
        if (fail) {
            return [];
        }
        for (let i = 0; i < p.length; i++) {
            if (count[p[i][1]] > 0) {
                remain.push(p[i]);
            }
        }
        p = remain;
    }
    return ans;
};
