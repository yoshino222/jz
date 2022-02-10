# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

# 示例 1：
#
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
# 示例 2：
#
# 输入：matrix =[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]

class Solution:
    def spiralOrder(self, matrix):
        lenth=len(matrix[0])
        high=len(matrix)
        quan=0
        ans=[]
        while lenth>0:
            for i in range(quan,lenth):
                ans.append(matrix[quan][i])
                print(ans)
            for j in range(quan+1,high):
                ans.append(matrix[j][lenth-1])
                print(ans)
            for z in range(quan+1,lenth):
                ans.append(matrix[high-quan-1][lenth-z-1])
                print(ans)
            for q in range(quan+1,high-1):
                ans.append(matrix[high-q-1][quan])
                print(ans)
            quan=quan+1
            lenth=lenth-1
            high=high-2
            print(quan,lenth,high)


matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
s=Solution()
print(s.spiralOrder(matrix))