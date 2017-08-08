/**
 * @param {number[][]} people
 * @return {number[][]}
 */
var reconstructQueue = function(people) {
    people.sort((a, b) => {
        if (a[1] === b[1]) return a[0] < b[0] ? -1 : 1;
        return a[1] < b[1] ? -1 : 1;
    });
    var a = [];
    for (var i=0; i<people.length; ++i) {
        var h = people[i][0];
        var j = 0;
        for (var k=people[i][1]; j<a.length; ++j) {
            if (h <= a[j][0]) {
                --k;
                if (k < 0) break;
            }
        }
        a.splice(j, 0, people[i]);
    }
    return a;
};
