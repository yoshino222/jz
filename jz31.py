class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack=[]
        i=0
        for num in pushed:
            stack.append(num)
            while stack and stack[-1]==popped[i]: #模拟栈 栈顶和popped一样 则出站
                stack.pop()
                i=i+1
        return not stack


