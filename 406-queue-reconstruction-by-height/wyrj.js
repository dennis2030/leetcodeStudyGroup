/**
 * @param {number[][]} people
 * @return {number[][]}
 */
var reconstructQueue = function(people) {
    people.sort((l, r) => {
        return (l[0] - r[0]) || (l[1] - r[1]);
    });
    for (let i = people.length - 1; i >=0; i--) {
        let person = people[i];
        let count = person[1];
        for (let j = i - 1; j >= 0; j--) {
            if (people[j][0] < people[i][0]) break;
            count--;
        }
        for (let j = i; j < i + count; j++) {
            people[j] = people[j + 1];
        }
        people[i + count] = person;
    }
    return people;
};
