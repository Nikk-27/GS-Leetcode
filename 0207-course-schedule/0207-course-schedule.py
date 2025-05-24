class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # it is cycle detection question , if cycle then False else True
        # cycle detection using DFS or BFS
        # BFS method also called Kahn's algo
        # Topological cycle is possible then its acyclic graph
        # Because topological sort only possible for DAG
        # DAG is directed acyclic graph

        def topocheck(numCourses, adjlist, indegree):
            q = deque()
            count = 0

            for i in range(numCourses):
                if indegree[i] == 0:
                    q.append(i)
                    count += 1
            while q:
                k = q.popleft()
                for i in adjlist[k]:
                    indegree[i] -= 1
                    if indegree[i] == 0:
                        q.append(i)
                        count += 1
            return count == numCourses


        indegree = [0] * numCourses
        adjlist = [[] for i in range(numCourses)]

        for a,b in prerequisites:
            # b --> a
            indegree[a] += 1
            adjlist[b].append(a)        

        return topocheck(numCourses, adjlist, indegree)

# TC = O(V + E), where V = numCourses, E:edges = len(prerequisites)
# SC = O(V + E)
