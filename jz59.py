#59 队列实现max_value 得到最大值

class MaxQueue:
    def __init__(self):
        self.res=[]
        self.value=0
        self.ans=[]
    def max_value(self):
        if not self.res:
            return -1
        else:
            return max(self.res)
    def push_back(self,value):
        self.res.append(value)
    def pop_front(self):



