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
    if (head === null) return null;
    let oneStep = head, twoStep = head;
    while (true) {
        if (twoStep.next === null || twoStep.next.next === null) return null;
        twoStep = twoStep.next.next;
        oneStep = oneStep.next;
        if (twoStep === oneStep) break;
    }
    oneStep = head;
    while (oneStep !== twoStep) {
        twoStep = twoStep.next;
        oneStep = oneStep.next;
    }
    return oneStep;
};