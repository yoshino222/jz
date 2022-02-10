class Solution:
    def twoSum(self, nums, target) :
        j=1
        ans=[]
        for i in range(len(nums)-2):
            while nums[i]+nums[j]<=target:

                if nums[i]+nums[j]==target:
                    ans.extend([nums[i],nums[j]])
                    return ans





s=Solution()
nums =[14,15,16,22,53,60]
target = 76
print(s.twoSum(nums,target))
