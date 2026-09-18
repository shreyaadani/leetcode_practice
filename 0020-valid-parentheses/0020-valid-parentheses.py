class Solution:
    def isValid(self, s: str) -> bool:
        db = {')':'(',']':'[','}':'{'}
        stack = []
        for i in s:
            if i in db and stack:
                if db[i] != stack.pop():
                    return False
            else:
                stack.append(i)


        return not stack                
            


