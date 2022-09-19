# 学校打算为全体学生拍一张年度纪念照。根据要求，学生需要按照 非递减 的高度顺序排成一行。
#
# 排序后的高度情况用整数数组 expected 表示，其中 expected[i] 是预计排在这一行中第 i 位的学生的高度（下标从 0 开始）。
#
# 给你一个整数数组 heights ，表示 当前学生站位 的高度情况。heights[i] 是这一行中第 i 位学生的高度（下标从 0 开始）。
#
# 返回满足 heights[i] != expected[i] 的 下标数量 。
#
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)#先排序

        return sum(1 for x, y in zip(heights, expected) if x != y)#zip 两两放入一个元祖 ，然后x，y进行比较

#计数排序
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        m = max(heights)
        cnt = [0] * (m + 1)

        for h in heights:
            cnt[h] += 1#h是高度，统计h高度的有几个

        idx = ans = 0
        for i in range(1, m + 1):#高度
            for j in range(cnt[i]):
                if heights[idx] != i:#按顺序，如果这个位置的人 身高和i不一样  就不对
                    ans += 1
                idx += 1#人数，位置移动

        return ans
