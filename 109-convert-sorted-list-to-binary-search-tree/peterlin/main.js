/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {TreeNode}
 */
var sortedListToBST = function(head) {
    if (head === null) {
        return null;
    }
    var f = (st, ed) => {
        if (st === ed) { return null; }
        var a = st, b = st;
        while (b !== ed && b.next !== ed) {
            a = a.next;
            b = b.next.next;
        }
        
        var r = new TreeNode(a.val);
        r.left = f(st, a);
        r.right = f(a.next, ed);
        return r;
    };
    return f(head, null);
};
