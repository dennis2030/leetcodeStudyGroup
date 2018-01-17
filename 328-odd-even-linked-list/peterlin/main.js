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
    if (head === null) return head;
    var n1 = head;
    var n2 = head.next;
    var h2 = n2;
    while (n2 !== null && n2.next !== null) {
        n1.next = n1.next.next;
        n2.next = n2.next.next;
        n1 = n1.next;
        n2 = n2.next;
    }
    
    n1.next = h2;
    return head;
};
