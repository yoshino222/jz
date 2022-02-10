# 输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。
#
# 示例 1:
#
# 输入: n = 1
# 输出: [1,2,3,4,5,6,7,8,9]
#  
#
# 说明：
#
# 用返回一个整数列表来代替打印
# n 为正整数
#
def pr(n):
    res=[]
    for i in range(1,pow(10,n)):
        res.append(i)
    return res
print(pr(2))
print(pr(1))

#大数的判断

class Solution:
    def printNumbers(self, n: int) -> [int]:
        def dfs(x):
            if x == n:
                s = ''.join(num[self.start:])
                if s != '0': res.append(s)
                if n - self.start == self.nine: self.start -= 1
                return
            for i in range(10):
                if i == 9: self.nine += 1
                num[x] = str(i)
                dfs(x + 1)
            self.nine -= 1

        num, res = ['0'] * n, []
        self.nine = 0
        self.start = n - 1
        dfs(0)
        return ','.join(res)


class Solution:
    def printNumbers(self, n: int) -> List[int]:
        def dfs(index, num, digit):
            if index == digit:#判断位数够了吗
                res.append(int(''.join(num)))
                return
            for i in range(10):
                num.append(str(i))#1-9放入num
                dfs(index + 1, num, digit)#下一位数
                num.pop()

        res = []#字符串list
        for digit in range(1, n + 1):#一共有n位，digit 表示位数
            for first in range(1, 10):#1到9开始循环
                num = [str(first)]#转成字符串 1,2,3,4,5,6,7,8,9
                dfs(1, num, digit)# dfs(1,1,1)从第一位开始  n次1-9的循环

        return res