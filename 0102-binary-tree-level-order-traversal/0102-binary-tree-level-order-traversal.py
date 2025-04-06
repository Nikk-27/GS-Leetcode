# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        final = []
        if not root:
            return final
        q = deque()
        q.append(root)

        while q:
            res = []
            for i in range(len(q)):
                node = q.popleft()
                if node is None:
                    return None
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                res.append(node.val)
            final.append(res)
        return final

# TC = O(N)
# SC = O(N)