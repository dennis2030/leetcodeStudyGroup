/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
	ListNode* removeNthFromEnd(ListNode* head, int n) {
		ListNode *first = head;
		ListNode **second = &head;

		for(int i = 1; i < n; ++i) {
			first = first->next;
		}

		while(first->next != NULL) {
			first = first->next;
			second = &((*second)->next);
		}

		*second = (*second)->next;
		return head;
	}
};
