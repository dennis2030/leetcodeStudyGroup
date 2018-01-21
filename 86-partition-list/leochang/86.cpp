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
    ListNode* partition(ListNode* head, int x) {
        ListNode* small = new ListNode(0);
        ListNode* big = new ListNode(0);
        ListNode* small_head = small;
        ListNode* big_head = big;
        while (head) {
            if (head->val < x) {
                small->next = head;
                small = small->next;
            } else {
                big->next = head;
                big = big->next;
            }
            head = head->next;
        }
        big->next = NULL;
        small->next = big_head->next;
        return small_head->next;
    }
};
