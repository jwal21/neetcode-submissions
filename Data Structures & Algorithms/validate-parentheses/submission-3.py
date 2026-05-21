class Solution:
    def isValid(self, s: str) -> bool:
        
        open2close = {')' : '(', ']' : '[', '}' : '{'}
        stack = []

        for c in s:

            if c in open2close:

                if stack and stack[-1] == open2close[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
            
        
        return True if not stack else False