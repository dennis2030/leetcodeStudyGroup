/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode *makeTreeFromNums(vector<int> &nums) {
        TreeNode *head = new TreeNode(nums[0]);

        for (auto iter = nums.begin() + 1; iter != nums.end(); ++iter) {
            TreeNode *curr = head;

            while (true) {
                if (*iter > curr->val) {
                    if (curr->right == NULL) {
                        curr->right = new TreeNode(*iter);
                        break;
                    }
                    curr = curr->right;
                } else { // *iter < curr->val
                    if (curr->left == NULL) {
                        curr->left = new TreeNode(*iter);
                        break;
                    }
                    curr = curr->left;
                }
            }
        }

        return head;
    }

    void generateTreesInner(vector<TreeNode*> &results, vector<int> &nums, stack<pair<int, int>> todo) {
        if (todo.empty()) {
            results.push_back(makeTreeFromNums(nums));
            return;
        }

        pair<int, int> range = todo.top();
        todo.pop();

        for (int i = range.first; i <= range.second; ++i) {
            int numNewTodo = 0;
            nums.push_back(i);

            if (i < range.second) {
                todo.push(make_pair(i + 1, range.second));
                ++numNewTodo;
            }
            if (i > range.first) {
                todo.push(make_pair(range.first, i - 1));
                ++numNewTodo;
            }

            generateTreesInner(results, nums, todo);

            nums.pop_back();
            for (int j = 0; j < numNewTodo; ++j) {
                todo.pop();
            }
        }
    }

    vector<TreeNode*> generateTrees(int n) {
        vector<TreeNode*> results;
        vector<int> nums;
        stack<pair<int, int>> todo;

        todo.push(make_pair(1, n));

        generateTreesInner(results, nums, todo);

        return results;
    }
};
