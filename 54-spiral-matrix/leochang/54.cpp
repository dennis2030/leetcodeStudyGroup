class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        if (matrix.empty()) return {};
        int m = matrix.size();
        int n = matrix[0].size();
        vector<int> ans(m*n);
        
        int col_left_bound = 0, row_top_bound = 0;
        int col_right_bound = n-1, row_bottom_bound = m-1;

        for (int c = 0; c < m*n;) {
            for (int i = col_left_bound; i <= col_right_bound; i++) {
                ans[c++] = matrix[row_top_bound][i];
            }
            row_top_bound++;
            for (int i = row_top_bound; i <= row_bottom_bound; i++) {
                ans[c++] = matrix[i][col_right_bound];
            }
            col_right_bound--;
            if (c == m*n) {
                break;
            }
            for (int i = col_right_bound; i >= col_left_bound; i--) {
                ans[c++] = matrix[row_bottom_bound][i];
            }
            row_bottom_bound--;
            for (int i = row_bottom_bound; i >= row_top_bound; i--) {
                ans[c++] = matrix[i][col_left_bound];
            }
            col_left_bound++;
        }
        return ans;
    }
};
