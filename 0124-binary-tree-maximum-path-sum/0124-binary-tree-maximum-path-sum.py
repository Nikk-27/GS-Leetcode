# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        if root is None:
            return 0
        
        # Recursively find the max path sum for the left and right subtrees
        left = self.solve(root.left)
        right = self.solve(root.right)
        
        # Path sum when including the current node and both children
        neeche_hi_milgaya_answer = left + right + root.val
        
        # Path sum when including the current node and one of its children
        koi_ek_acha = max(left, right) + root.val
        
        # Path sum when only the current node is considered
        only_root_acha = root.val
        
        # Update the global maxSum considering the possible paths through this node
        self.maxSum = max(self.maxSum, neeche_hi_milgaya_answer, koi_ek_acha, only_root_acha)
        
        # Return the maximum path sum that can be extended to the parent node
        return max(koi_ek_acha, only_root_acha)
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float('-inf')  # Reset maxSum for a new tree
        self.solve(root)  # Start the recursive process
        return self.maxSum  # Return the result can we do it in this manner
        