class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxlen = 0
        maxfreq = 0
        l = 0
        count = {}

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)
            maxfreq = max(maxfreq,count[s[r]])

            if (r - l + 1) - maxfreq > k:
                count[s[l]] -= 1
                l+= 1

            maxlen = max(maxlen,r-l+1)    
        

        return maxlen


        