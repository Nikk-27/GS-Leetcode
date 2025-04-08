class Solution:
    def cyclicDFS(self, i, adjlist, visited, inrecursion):
        visited[i] = True
        inrecursion[i] = True

        for v in adjlist[i]:
            if not visited[v] and self.cyclicDFS(v, adjlist, visited, inrecursion):
                return True
            elif inrecursion[v]:  # still in recursion stack
                return True

        inrecursion[i] = False  # done with this node
        return False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist = [[] for _ in range(numCourses)]
        visited = [False] * numCourses
        inrecursion = [False] * numCourses

        for a, b in prerequisites:
            # b --> a (to take course a, you must finish b)
            adjlist[b].append(a)

        for i in range(numCourses):
            if not visited[i] and self.cyclicDFS(i, adjlist, visited, inrecursion):
                return False  # cycle found, cannot finish courses
        return True  # no cycle, safe to finish all courses
