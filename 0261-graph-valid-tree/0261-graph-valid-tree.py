class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        if len(edges) != n-1 :
            return False

        adj = [[] for _ in range(n)]
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        seen = {0}
        queue = deque([0])

        while queue:
            node = queue.popleft()
            for nbr in adj[node]:
                if nbr in seen:
                    continue
                seen.add(nbr)
                queue.append(nbr)

        return len(seen) == n                    
        