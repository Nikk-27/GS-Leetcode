# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def checkbst(root, minvalue, maxvalue):
            if not root:
                return True
            
            if not (minvalue < root.val < maxvalue):
                return False

            left_valid = checkbst(root.left, minvalue, root.val)
            right_valid = checkbst(root.right, root.val, maxvalue)

            return left_valid and right_valid

        return checkbst(root, float('-inf'), float('inf'))

#  TC = O(N)
#  SC = O(N) in worst case unbalanced tree
    # = O(logN) in best case balanced tree
        