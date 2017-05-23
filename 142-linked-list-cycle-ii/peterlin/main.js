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
var detectCycle = function(head) {
    var a = head, b = head;
    while(true) {
        if (a === null || a.next === null) return null;
        a = a.next.next;
        b = b.next;
        if (a === b) {
            var c = head;
            while (b !== c) {
                b = b.next;
                c = c.next;
            }
            return c;
        }
    }
};
