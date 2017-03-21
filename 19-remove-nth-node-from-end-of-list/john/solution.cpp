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
        ListNode *behind = head;
        ListNode *front = head;

        for (int i = 0; i < n; ++i) {
            front = front->next;
        }

        if (front == NULL) {
            head = behind->next;
            free(behind);
            return head;
        }

        while (front->next != NULL) {
            behind = behind->next;
            front = front->next;
        }

        ListNode *removed = behind->next;
        behind->next = removed->next;
        free(removed);
        return head;
    }
};
