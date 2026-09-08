class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        res = 0 
        if len(s) < k:
            return 0

        freq = Counter(s)
        for c in freq:
            if  freq[c] < k:
                return max(self.longestSubstring(piece, k) for piece in s.split(c))

        return len(s)       
                  
        
