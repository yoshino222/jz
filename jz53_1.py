#统计一个数字在排序数组中出现的次数。
class Solution:
    def search(self, nums, target) :
        #return nums.count(target)
        def fuc(tar):
            left,right=0,len(nums)-1
            while left<=right:
                pos=(left+right)//2
                if nums[pos]<=tar:left=pos+1
                else:right=pos-1
            return left
        return fuc(target)-fuc(target-1)


nums = [5, 7, 7, 8, 8, 10]
target = 8
s=Solution()
print(s.search(nums,target))
