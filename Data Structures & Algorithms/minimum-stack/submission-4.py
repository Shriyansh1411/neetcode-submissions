from collections import deque

class MinStack:

    def __init__(self):
        self.queue=deque([])
        self.min_queue=[]

    def push(self, val: int) -> None:
        self.queue.append(val)
        if len(self.min_queue)==0 or val<=self.min_queue[-1]:
            self.min_queue.append(val)
         


    def pop(self) -> None:
        if (len(self.queue)==0):
            return "THE STACK IS EMPTY"
        
        element= self.queue.pop()
        if (element == self.min_queue[-1]):
            self.min_queue.pop()

    def top(self) -> int:
        if (len(self.queue)==0):
            return "THE STACK IS EMPTY"
        return self.queue[-1]
        

    def getMin(self) -> int:
        if (len(self.queue)==0):
            return "THE STACK IS EMPTY"
        return self.min_queue[-1]   