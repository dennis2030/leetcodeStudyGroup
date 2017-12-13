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
    let p = new ListNode(0), q = new ListNode(0), pp, qq;
    for(pp=p, qq=q;head !== null;head = head.next) {
        if (head.val < x) {
            pp.next = head;
            pp = head;
        } else {
            qq.next = head;
            qq = head;
        }
    }
    pp.next = q.next;
    qq.next = null;
    return p.next;
};
