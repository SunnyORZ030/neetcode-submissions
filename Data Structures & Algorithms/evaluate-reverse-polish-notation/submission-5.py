class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ansStack = []

        for i in tokens:
            if i == '+': 
                a = ansStack.pop()
                b = ansStack.pop()
                result = a + b
                ansStack.append(result)
            elif i == '-':
                a = ansStack.pop()
                b = ansStack.pop()
                result = b - a
                ansStack.append(result) 
            elif i == '*':
                a = ansStack.pop()
                b = ansStack.pop()
                result = a * b
                ansStack.append(result)
            elif i == '/':
                a = ansStack.pop()
                b = ansStack.pop()
                result = int(b / a)
                ansStack.append(result)
            else:
                ansStack.append(int(i))

        return ansStack[0]