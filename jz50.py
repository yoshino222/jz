class Solution:
    def firstUniqChar(self, s):
        ans={}
        for a in s:#
            ans[a]=not a in ans#a不在ans里就是true，在ans里就是false
        for a in s:
            if ans[a]:
                return a
        return " "
a={"A":12,"b":33}
c=Solution()
s = "abaccdeff"
print(c.firstUniqChar(s))