class Solution {
public:    
    vector<int> findDiagonalOrder(vector<vector<int>>& matrix) {
        if (matrix.size() == 0 || matrix[0].size() == 0) {
            return std::vector<int>();
        }
        
        size_t num_row = matrix.size();
        size_t num_col = matrix[0].size();
        std::vector<int> ans;
        
        size_t current_sum = 0;
        size_t row, col;
        while (current_sum < num_row + num_col) {
            for (size_t i = 0; i <= current_sum; i++) {
                if (current_sum % 2 == 1) {
                    row = i;
                    col = current_sum - i;
                } else {
                    row = current_sum - i;
                    col = i;
                }
                if (row < num_row && col < num_col) {
                    ans.push_back(matrix[row][col]);
                }
            }            
            current_sum++;
        }
        return ans;
    }
};
