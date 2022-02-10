import unittest
class Solution():
    def puke(self,nums):
        carry=0
        nums.sort()
        print(nums)
        for i in range(4):
            print(nums[i])
            if nums[i]==0:carry=carry+1
            if nums[i]==nums[i+1] and nums[i]!=0:return False
        print(nums[carry])
        if nums[4]-nums[carry]<5:return True




ask=[4,7,5,9,2]
s=Solution()
print(s.puke(ask))