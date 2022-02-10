# 输入一个字符串，打印出该字符串中字符的所有排列。
class Solution:
    def permutation(self, s: str) :
        c=list(s)
        ans=[]

        def dfs(x):
            if x==len(c)-1:
                ans.append(''.join(c))
                return
            dic=set()
            for i in range(x,len(c)):
                if c[i] in dic:
                    continue
                dic.add(c[i])
                c[i],c[x]=c[x],c[i]




s="abc"
so=Solution()