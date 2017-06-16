/**
 * @param {number[][]} matrix
 * @param {number} k
 * @return {number}
 */
var kthSmallest = function(matrix, k) {
    var n = matrix.length;
    
    var upper_bound = (arr, x) => {
        var m, l = 0, r = arr.length-1;
        while (l<=r) {
            m = Math.floor((l+r)/2);
            if (x >= arr[m]) l = m+1;
            else r = m-1;
        }
        return l;
    };
    
    var low = matrix[0][0];
    var high = matrix[n-1][n-1];
    while (low < high) {
        var mid = Math.floor((low+high)/2);
        
        var cnt = 0;
        for (var i=0;i<n;++i) {
            cnt += upper_bound(matrix[i], mid);
        }
        
        if (cnt < k) {
            low = mid+1;
        } else {
            high = mid;
        }
    }
    return low;
};
