# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def count_node(self, head):
        length = 0
        node = head
        while node != None:
            length += 1
            node = node.next
        return length
    
    def construct_tree(self, node_num):        
        if node_num <= 0:
            return None
        head = TreeNode(None)
        import Queue
        q = Queue.Queue()
        
        idx = 1
        node = head
        
        while True:
            if node_num == idx:
                break
            if node.left == None:
                tmp_node = TreeNode(None)
                q.put(tmp_node)
                node.left = tmp_node                
                idx += 1
            elif node.right == None:
                tmp_node = TreeNode(None)
                q.put(tmp_node)
                node.right = tmp_node                
                idx += 1
            else:
                node = q.get()            
                
        return head        
    
    def fill_value(self, treeNode, listNode):
        
        if treeNode.left != None:            
            listNode = self.fill_value(treeNode.left, listNode)
                
        treeNode.val = listNode.val
        listNode = listNode.next
        
        if treeNode.right != None:
            listNode = self.fill_value(treeNode.right, listNode)
        
        return listNode
    
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        num = self.count_node(head)
        if num <= 0:
            return []
        treeHead = self.construct_tree(num)
        self.fill_value(treeHead, head)
        return treeHead
        
