/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {number[]}
 */
var findOrder = function(numCourses, prerequisites) {
    let sol = true;
    const a = [];
    const m = new Map();
    const r = Array(numCourses).fill().map(x => Array(numCourses).fill(false));
    const f = (x) => {
        if (m.has(x)) {
            if (m.get(x) === 1) sol = false;
            return;
        }
        m.set(x, 1);
        for (let i=0;i<numCourses;++i) {
            if (r[i][x]) {
                f(i);
            }
        }
        a.push(x);
        m.set(x, 2);
    };
    
    prerequisites.forEach((p) => {
        r[p[0]][p[1]] = true;
    });
    
    for (let i=0,j;i<numCourses;++i) {
        for (j=0;j<numCourses && !r[i][j];++j);
        if (j === numCourses) {
            f(i);
        }
    }
    return sol && a.length === numCourses ? a.reverse() : [];
};
