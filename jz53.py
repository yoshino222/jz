#一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。


class Solution:
    def missingNumber(self, nums) :
        rh=0
        lh=len(nums)-1
        while rh<lh:
            n=(rh+lh)//2
            if nums[n]==n:rh=n+1
            else:lh=n-1
        return rh
s=Solution()
nums=[0,1,2,3,4,5,6,7,9]
print(s.missingNumber(nums))
