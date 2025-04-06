# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        if not root and not subRoot:
            return True
        
        if self.sametree(root, subRoot):
            return True
        
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    def sametree(self, root, subRoot):
        if not root and not subRoot:
            return True
        if root and subRoot and root.val == subRoot.val:
            return self.sametree(root.left, subRoot.left) and self.sametree(root.right, subRoot.right) 
        return False

# TC = O(m * n) 
# SC = O(m + n) recursion stack of both trees

# Where m is the number of nodes in subRoot and n is the number of nodes in root.