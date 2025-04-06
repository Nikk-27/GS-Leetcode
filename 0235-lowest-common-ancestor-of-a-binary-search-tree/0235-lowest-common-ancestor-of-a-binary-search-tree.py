# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root
        
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur

'''
TC: of the lowestCommonAncestor function is O(h), where 
ℎ is the height of the binary search tree. In the worst case, this could be \U0001d442(\U0001d441) for a skewed tree, where \U0001d441 is the number of nodes. However, for a balanced tree, it would be \U0001d442(logN).

Space Complexity:
The space complexity is O(1) since the solution only uses a constant amount of extra space for variables like cur 
'''