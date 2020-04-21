# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        
        def helper(preorder, limit):
            if preorder and preorder[0] < limit:
                val = preorder.pop(0)
                node = TreeNode(val)
                node.left = helper(preorder, val)
                node.right = helper(preorder, limit)
                return node
            return None
        res = helper(preorder, float('inf'))
        return res
