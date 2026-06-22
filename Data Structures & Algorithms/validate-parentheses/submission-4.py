class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ')':'(',
            ']':'[',
            '}':'{'
        }

        stack = []

        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            elif ch is '(' or '[' or '{':
                stack.append(ch)

        return not stack