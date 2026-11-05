class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        n = len(s)
        buckets = [[] for _ in range(n+1)]
        res = []

        for k,v in freq.items():
            buckets[v].append(k)

        for i in range(n,0,-1):
            for j in buckets[i]:
                res.append(j*i)


        return "".join(res)        

        