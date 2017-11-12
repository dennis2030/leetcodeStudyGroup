class Solution {
public:
    vector<vector<char>> updateBoard(vector<vector<char>>& board, vector<int>& click) {
        if(board[click[0]][click[1]] == 'M'){
            board[click[0]][click[1]] = 'X';
            return board;
        }
        dfs(board, click[0], click[1]);
        return board;
    }
    void dfs(vector<vector<char>>& board, int x, int y) {       
        int count = 0;
        if (board[x][y] == 'E') {
            for (int i = -1; i <= 1; i++) {
                for (int j = -1; j <= 1; j++) {
                    if (i == 0 && j == 0) {
                        continue;
                    }
                    if (x+i < 0 || x+i >= board.size() ||
                       y+j < 0 || y+j >= board[0].size()) {
                        continue;
                    }
                    if (board[x+i][y+j] == 'M' || board[x+i][y+j] == 'X') {
                        count++;
                    }
                }
            }
        
            if (count > 0) {
                board[x][y] = '0' + count;
            } else {
                board[x][y] = 'B';         
                for (int i = -1; i <= 1; i++) {
                    for (int j = -1; j <= 1; j++) {
                        if (i == 0 && j == 0) {
                            continue;
                        }
                        if (x+i < 0 || x+i >= board.size() ||
                           y+j < 0 || y+j >= board[0].size()) {
                            continue;
                        }
                        dfs(board, x+i, y+j);
                    }
                }
            }
        }
    }
};
