/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var oddEvenList = function(head) {
    if (!head || !head.next || !head.next.next) return head;
    let tail = head;
    let pre = head.next;
    let curr = pre.next;
    let flag = true;
    while (curr) {
        if (!flag) {
            pre = pre.next;
        } else {
            pre.next = curr.next;
            curr.next = tail.next;
            tail.next = curr;
            tail = curr;
        }
        curr = pre.next;
        flag = !flag;
    }
    return head;
};
