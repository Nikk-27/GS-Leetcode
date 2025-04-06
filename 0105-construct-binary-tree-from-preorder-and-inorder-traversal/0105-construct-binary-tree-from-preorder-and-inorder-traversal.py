# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    # Create a hash map to store the index of each value in inorder
        inorder_map = {value: index for index, value in enumerate(inorder)}
        
        def helper(pre_start, in_start, in_end):
            if pre_start > len(preorder) - 1 or in_start > in_end:
                return None
            
            # The root is the first element in preorder
            root_val = preorder[pre_start]
            root = TreeNode(root_val)
            
            # Find the index of the root in inorder using the hash map
            in_index = inorder_map[root_val]
            
            # Recursively build left and right subtrees
            root.left = helper(pre_start + 1, in_start, in_index - 1)
            root.right = helper(pre_start + in_index - in_start + 1, in_index + 1, in_end)
            
            return root
        
        return helper(0, 0, len(inorder) - 1)