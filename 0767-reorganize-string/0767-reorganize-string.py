class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxcount, letter = 0,''
        res= ['']*len(s)

        for char, cnt in count.items():
            if cnt > maxcount:
             maxcount = cnt
             letter = char

        if maxcount > (len(s) + 1) // 2  :
         return ""

        index = 0

        # placing max freq:
        while count[letter] !=0:
            res[index] = letter
            index += 2
            count[letter]-=1

        for c , f in count.items():
         while f > 0:
            if index >= len(s):
                index = 1
            res[index] = c
            index+=2
            f -=1

        return ''.join(res)    



            
        