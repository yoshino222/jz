# 剑指Offer30.包含min函数的栈
# 定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的min函数在该栈中，调用min、push及pop的时间复杂度都是O(1)。
#
# 示例:
#
# MinStack
# minStack = new
# MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.min();
# --> 返回 - 3.
# minStack.pop();
# minStack.top();
# --> 返回
# 0.
# minStack.min();
# --> 返回 - 2.
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.dataA=[]
        self.dataB=[]#b用来储存min

    def push(self, x: int) -> None:
        self.dataA.append(x)#放进数字
        if not self.B or self.B[-1]>=x:#判断最新的数字大小是不是比b的顶部小，小的话放进b
            self.dataB.append(x)
    def pop(self) -> None:
        if self.dataA.pop==self.dataB[-1]:
            self.dataB.pop()#如果弹出的数字 也是当前的最小值，b也弹出

    def top(self) -> int:
        return self.dataA[-1]
    def min(self) -> int:
        return self.dataB[-1]#b的栈顶，也就是list尾 是当前最小值



