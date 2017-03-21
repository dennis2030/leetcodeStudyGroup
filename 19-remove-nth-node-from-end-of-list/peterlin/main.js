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
    var a = head;
    var b = head;
    for (;n>0;--n) a = a.next;
    while (a !== null && a.next !== null) {
        a = a.next;
        b = b.next;
    }
    if (a === null) {
        if (b.next === null) {
            return null;
        }
        b.val = b.next.val;
    }
    b.next = b.next.next;
    return head;
};
