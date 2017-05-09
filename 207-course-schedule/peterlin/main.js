/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */
var canFinish = function(numCourses, prerequisites) {
    var c = true;
    var p = {};
    var m = {};
    var f = (src, cur) => {
        if (!c) return;
        p[cur] = true;
        
        m[cur].forEach((next) => {
            if (next == src) {
                c = false;
                return;
            }
            if (!(next in p)) f(src, next);
        });
    }
    
    for(var i=0;i<numCourses;++i) m[i] = [];
    for(var k in prerequisites) {
        var req = prerequisites[k];
        m[req[0]].push(req[1]);
    }
    
    for(var i=0;i<numCourses;++i){
        p = {};
        f(i, i);
    }
    return c;
};
