class Solution():
    def two(self,nums):
        key={}
        ans=[]
        for num in nums:
            key[num]=not num in key
        for num in nums:
            if key[num]:
                ans.append(num)
        return ans

nums=[4,1,4,6]
s=Solution()
print(s.two(nums))