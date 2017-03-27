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
var insertionSortList = function(head) {
    let it = head;
    while (it && it.next) {
        let next = it.next;
        if (next.val < head.val) {
            it.next = next.next;
            next.next = head;
            head = next;
        } else if (next.val < it.val) {
            let pre = head;
            while (pre.next.val < next.val) {
                pre = pre.next;
            }
            it.next = next.next;
            next.next = pre.next;
            pre.next = next;
        } else {
            it = it.next;
        }
    }
    return head;
};