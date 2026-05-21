class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        closeToOpen = {")" : "(", "]" : "[", "}" : "{"}

        for c in s:
            # checking if is close bracket (key in hashmap)
            if c in closeToOpen:
                # check that stack isnt empty, and top of stack is the corresponding open bracket
                if stack and stack[-1] == closeToOpen[c]:
                    # remove top element in stack
                    stack.pop()
                # otherwise the parentheses do not match
                else:
                    return False
            
            # if not a close bracket, add it to the stack (open bracket)
            else:
                stack.append(c)
        
        # if the stack is empty this means all parenthesese are valid
        return True if not stack else False
                