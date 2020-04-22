import sys
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minval = sys.maxsize

    def push(self, x: int) -> None:
        if x <= self.minval:
            self.stack.append(self.minval)
            self.minval = x
        self.stack.append(x)

    def pop(self) -> None:
        if self.stack and self.stack.pop() == self.minval:
            self.minval = self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minval


# Your MinStack object will be instantiated and called as such:
#obj = MinStack()
#obj.push(x)
#obj.pop()
#param_3 = obj.top()
#param_4 = obj.getMin()
