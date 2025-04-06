"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        
        def bfs(node):
            q = deque()
            q.append(node)

            oldtoNew = {}
            oldtoNew[node] = Node(int(node.val))

            while q:
                cur = q.popleft():
                for i in cur.neighbors:
                    if i not in oldtoNew:
                        oldtoNew[i] = Node(int(i.val))
                        q.append(i)
                    oldtoNew[cur].neighbors.append(oldtoNew[i])
            return oldtoNew[node]

        return bfs(node)
