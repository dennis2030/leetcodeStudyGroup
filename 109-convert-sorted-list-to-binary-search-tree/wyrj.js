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
    let arr = [], curr = head;
    while (curr !== null) {
        arr.push(curr.val);
        curr = curr.next;
    }
    function createTree(s, e) {
        if (s > e) return null;
        let m = Math.ceil((s + e) / 2);
        let node = new TreeNode(arr[m]);
        node.left = createTree(s, m - 1);
        node.right = createTree(m + 1, e);
        return node;
    }
    return createTree(0, arr.length - 1);
};
