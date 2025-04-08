class Solution:

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # we need to return topological sort order
        # i am doing it with Kahn's algo

        adjlist = [[] for i in range(numCourses)]
        indegree = [0] * numCourses

        for a, b in prerequisites:
            # b --> a
            adjlist[b].append(a)
            indegree[a] += 1
        
        q = deque()
        output = []
        finish = 0

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
                output.append(i)
                finish += 1
                
        while q:
            u = q.popleft()
            for v in adjlist[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
                    output.append(v)
                    finish += 1
        
        return output if finish == numCourses else []

# TC = O(V + E)
# SC = O(V + E)



    

