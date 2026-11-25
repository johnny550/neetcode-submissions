class HistoryNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.next= next
        self.prev = prev

class BrowserHistory:
    # doubly linked list
    def __init__(self, homepage: str):
        self.head = HistoryNode(homepage)
        

    def visit(self, url: str) -> None:
        # add new node at end
        self.head.next=HistoryNode(url,self.head)
        self.head = self.head.next
        

    def back(self, steps: int) -> str:
        # for _ in range(steps):
        #     self.head = self.head.prev
        while self.head.prev and steps>0:
            self.head = self.head.prev
            steps-=1
        return self.head.val
        

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.head.next:
                self.head = self.head.next
        # while self.head.next and steps>0:
        #     self.head = self.head.next
        #     steps-=1
        return self.head.val

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)