class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        q = deque()
        Visited = 0

        for p in prerequisites:
            adj[p[1]].append(p[0])
            indegree[p[0]] +=1  #left to right 1->0
        

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        while q:
            node = q.popleft()
            Visited +=1
            for prereq in adj[node]:
                indegree[prereq] -= 1
                if indegree[prereq] == 0:
                    q.append(prereq)

        print(Visited)
        return Visited == numCourses                   



