class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        m = min(strs)
        res = inf
        
        for s in strs:
            match=0
            for i in range(len(m)):
                if m[i] == s[i]:
                    match+=1
                else:
                    break
            res= min(res,match)
        print(res)
        if res == inf:
            return ""

        return m[:res]           

