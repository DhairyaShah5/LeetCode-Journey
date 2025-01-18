class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        newStack = []

        for token in tokens:
            if token.lstrip('-').isdigit():
                newStack.append(int(token))
            elif token == '+':
                val1 = newStack.pop()
                val2 = newStack.pop()
                newStack.append(val1 + val2)
            elif token == '*':
                val1 = newStack.pop()
                val2 = newStack.pop()
                newStack.append(val1 * val2)
            elif token == "/":
                val1 = newStack.pop()
                val2 = newStack.pop()
                newStack.append(int(val2 / val1))
            elif token == "-":
                val1 = newStack.pop()
                val2 = newStack.pop()
                newStack.append(val2 - val1)

        return newStack[0]
