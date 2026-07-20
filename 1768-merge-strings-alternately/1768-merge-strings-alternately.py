class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        n = len(word1)
        m = len(word2)
        q = min(n,m)
        for i in range(0,q):
            res.append(word1[i])
            res.append(word2[i])
        if q == n:
            res.append(word2[q:]) 
        else:
            res.append(word1[q:])

        return "".join(res)            


        
        