#59 队列实现max_value 得到最大值
import queue
class MaxQueue:
    def __init__(self):
        self.queue=queue.queue
        self.deque=queue.deque
    def max_value(self):
        if not self.deque:
            return -1
        else:
            return self.deque(0)
    def push_back(self,value):
        self.queue.append(value)
        while self.deque and self.deque(0)>value:
            self.deque.append(value)
    def pop_front(self):
        if self.queue(0)==self.deque(0):
            self.queue.pop(0)
            return self.deque.pop(0)
        else:
            return self.queue.pop(0)



