from collections import deque
class MinStack:

    def __init__(self):
        # self.stack=deque()
        self.stack=[]

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        # self.stack.pop()
        self.stack=self.stack[0:len(self.stack)-1]
        # print(f" after pop {self.stack}")
        
    def top(self) -> int:
        print(self.stack)
        return self.stack[-1]
        
    def getMin(self) -> int:
        return min(self.stack)
        
