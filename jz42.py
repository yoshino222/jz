class Solution:
    def maxSubArray(self, nums):
        h=[]
        h.append(nums[0])
        for i in range(1,len(nums)):
            if h[i-1]<0:
                h.append(nums[i])
            else:
                h.append(h[i-1]+nums[i])
        return max(h)

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
s=Solution()
print(s.maxSubArray(nums))