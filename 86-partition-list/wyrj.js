/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} x
 * @return {ListNode}
 */
var partition = function(head, x) {
    if (!head) return head;
    let pc = head;
    let pp = null;
    while (pc) {
        if (pc.val >= x) {
            break;
        }
        pp = pc;
        pc = pc.next;
    }
    let curr = pc;
    let pre = pp;
    while (curr) {
        if (curr.val < x) {
            pre.next = curr.next;
            curr.next = pc;
            if (pp) {
                pp.next = curr;
            } else {
                head = curr;
            }
            pp = curr;
        } else {
            pre = curr;
        }
        curr = pre.next;
    }
    return head;
};
