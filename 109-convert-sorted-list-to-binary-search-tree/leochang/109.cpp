/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
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
	TreeNode* sortedListToBST(ListNode* head) {
		if (head == NULL) {
			return NULL;
		}
		return recursivetoBST(head, NULL);
	}
private:
	TreeNode* recursivetoBST(ListNode *head, ListNode *tail){
		if (head == tail) {
			return NULL;
		}
		ListNode *slow = head, *fast = head;
		while (fast != tail && fast->next != tail) {
			slow = slow->next;
			fast = fast->next->next;
		}
		TreeNode *root = new TreeNode(slow->val);
		root->left = recursivetoBST(head, slow);
		root->right = recursivetoBST(slow->next, tail);
		return root;
	}
};
