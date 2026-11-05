from collections import deque
class MinStack:

    def __init__(self):
        self.stack=[]
        self.min_stack=[]
        new_min=0

    def push(self, val: int) -> None:
        self.stack.append(val)
        try:
            el=self.get_last(self.min_stack)
            self.new_min=min(el,val)
            # print(f"picked between : {val, el}")
        except IndexError:
            self.new_min = val
        self.min_stack.append(self.new_min)
        # print(f"new min: {self.new_min}")
        # print(f"min list {self.min_stack}")
    
    def get_last(self,st) -> int:
        return st[-1]
        

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        # print(f"after popping {self.stack}")
        # print(f"after min popping {self.min_stack}")
        
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        # print(f"len {len(self.min_stack)}")
        return self.min_stack[-1] 
        
