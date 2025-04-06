# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BFS
        
        q = deque()
        q.append(root)
        res = []
        if root is None:
            return res

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node is None:
                    return None
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(node.val)
        return res

# TC = O(N)
# SC = O(N)
