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
	ListNode *detectCycle(ListNode *head) {
		if (head == NULL || head->next == NULL || head->next->next == NULL) {
			return NULL;
		}

		ListNode *first = head;
		ListNode *second = head;

		while (first->next != NULL && first->next->next != NULL) {
			first = first->next->next;
			second = second->next;
			if (first == second) {
				first = head;
				while (first != second) {
					first = first->next;
					second = second->next;
				}
				return first;
			}
		}
		return NULL;
	}
};
