# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def goes_down(node,high):
            if not node:
                return 0
            good_node = 0
            if high <= node.val:
                high = node.val
                good_node += 1
            good_node += goes_down(node.left,high)
            good_node += goes_down(node.right,high)
            return good_node
        return goes_down(root, -101)