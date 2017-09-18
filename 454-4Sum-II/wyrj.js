/**
 * @param {number[]} A
 * @param {number[]} B
 * @param {number[]} C
 * @param {number[]} D
 * @return {number}
 */
var fourSumCount = function(A, B, C, D) {
    function twoSum(arr1, arr2) {
        let arr = [];
        for (let i = 0; i < arr1.length; i++) {
            for (let j = 0; j < arr2.length; j++) {
                arr.push(arr1[i] + arr2[j]);
            }
        }
        arr.sort((l, r) => (l - r));
        let len = 0, o = {value: void 0, count: 0};
        for (let i = 0; i < arr.length; i++) {
            if (arr[i] === o.value) {
                o.count += 1;
            } else {
                o = {value: arr[i], count: 1};
                arr[len] = o;
                len += 1;
            }
        }
        arr.length = len;
        return arr;
    }
    let a1 = twoSum(A, B);
    let a2 = twoSum(C, D);
    let count = 0, i = 0, j = a2.length - 1;
    while (i < a1.length && j >= 0) {
        let v = a1[i].value + a2[j].value;
        if (v < 0) i += 1;
        else if (v > 0) j -= 1;
        else {
            count += a1[i].count * a2[j].count;
            i += 1;
            j -= 1;
        }
    }
    return count;
    
};
