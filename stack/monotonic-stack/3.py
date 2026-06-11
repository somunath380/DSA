# https://leetcode.com/problems/min-stack/description/

class MinStack:

    def __init__(self):
        self.mono_stack=[]
        self.min=[]

    def push(self, value: int) -> None:
        self.mono_stack.append(value)
        if not self.min:
            self.min.append(value)
        elif self.min[-1]>value:
            self.min.append(value)
        else:
            self.min.append(self.min[-1])

    def pop(self) -> None:
        self.mono_stack.pop()
        self.min.pop()

    def top(self) -> int:
        return self.mono_stack[-1]
    
    def getMin(self) -> int:
        return self.min[-1]

min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)
min_stack.getMin()
min_stack.pop()
min_stack.top()
min_stack.getMin()