class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        nset = set()
        l,r = 0,0
        res = 0

        for r in range(len(s)):
            while s[r] in nset:
                nset.remove(s[l])
                l+=1
            nset.add(s[r])
            res = max(res,r-l+1)


        return res              
    


        