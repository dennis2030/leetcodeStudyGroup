/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function(head, n) {
    var start = head, end = head;
    while(0 < n) {
        n--;
        end = end.next;
    }
    if (null === end) {
        return (head) ? head.next : head;
    }
    while(null !== end.next) {
        start = start.next;
        end = end.next;
    }
    start.next = start.next.next;
    return head;
};