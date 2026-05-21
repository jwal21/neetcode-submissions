class Solution:
    def isValid(self, s: str) -> bool:
        
        closetoOpen = { ']' : '[', '}' : '{', ')' : '(' }
        stack = []

        for char in s:
            
            if char in closetoOpen:
                if stack and stack[-1] == closetoOpen[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False
        
            
            
            