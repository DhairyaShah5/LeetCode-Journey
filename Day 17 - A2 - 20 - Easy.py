class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in '({[':
                stack.append(char)
            elif char in ')}]':
                if not stack:
                    return False
                    break
                top = stack.pop()
                
                if char == ')' and top != '(':
                    return False
                    break
                if char == '}' and top != '{':
                    return False
                    break
                if char == ']' and top != '[':
                    return False
                    break
                
        else:
            if not stack:
                return True
            else:
                return False