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
    var a = null;
    for (;head !== null;head = head.next) {
        var c = new ListNode(head.val);
        if (a === null) {
            a = c;
            continue;            
        }
        if (a.val > c.val) {
            c.next = a;
            a = c;
            continue;
        }
        var i = a;
        while (true) {
            if (i.next === null) { 
                i.next = c;
                break;
            }
            if (i.next.val >= c.val) {
                c.next = i.next;
                i.next = c;
                break;
            }
            i = i.next;
        }
    }
    return a;
};
