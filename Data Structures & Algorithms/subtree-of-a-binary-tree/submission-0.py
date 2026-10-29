# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtreeRoot(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None and root is None:
            return True
        if subRoot is None:
            return False
        if root is None:
            return False
        if root.val == subRoot.val:
            return self.isSubtreeRoot(root.left,subRoot.left) and self.isSubtreeRoot(root.right, subRoot.right)
        return False
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None and root is None:
            return True
        if subRoot is None:
            return False
        if root is None:
            return False
        return self.isSubtreeRoot(root,subRoot) or self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        
        