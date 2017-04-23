#include <cstdio>
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
	ListNode* insertionSortList(ListNode* head) {
		if (!head) {
			return head;
		}

		ListNode* current_head = head;
		ListNode* next_node = NULL;
		ListNode* new_head = new ListNode(0);

		while (current_head) {
			next_node = current_head->next;
			ListNode* prev_node = new_head;

			while (prev_node->next && prev_node->next->val < current_head->val) {
				prev_node = prev_node->next;
			}

			current_head->next = prev_node->next;
			prev_node->next = current_head;
			current_head = next_node;
		}

		return new_head->next;
	}
};
