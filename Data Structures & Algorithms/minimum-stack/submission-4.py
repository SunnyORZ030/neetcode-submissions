class MinStack:

    def __init__(self):
        self.stack = []
        self.MinStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.MinStack:
            self.MinStack.append(val)
        elif val < self.MinStack[-1]:
            self.MinStack.append(val)
        else:
            self.MinStack.append(self.MinStack[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.MinStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.MinStack[-1]
