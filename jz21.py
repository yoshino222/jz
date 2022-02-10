# 21.
# 调整数组顺序使奇数位于偶数前面
# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。
#
# 示例：
#
# 输入：nums = [1, 2, 3, 4]
# 输出：[1, 3, 2, 4]
# 注：[3, 1, 2, 4]
# 也是正确的答案之一。
#

# 提示：
#
# 0 <= nums.length <= 50000
# 1 <= nums[i] <= 10000

#解法  从两端往中间  或 两指针从一端开始
def exchange(nums):
    i=0
    for j in range(len(nums)):
        if nums[i]%2==0 and nums[j]%2==1 and i<j:
            nums[i],nums[j]=nums[j],nums[i]
            i=i+1
        if nums[i]%2==1:
            i=i+1
    return nums


nums=[1,2,3,4]
print(exchange(nums))




