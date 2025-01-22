class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        paths = path.split('/')

        for string in paths:
            if string == '..':
                if stack:
                    stack.pop()
            elif string != '' and string != '.':
                stack.append(string)

        return '/' + '/'.join(stack)