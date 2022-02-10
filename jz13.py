# 地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），
# 也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19
# 。请问该机器人能够到达多少个格子？
# 示例 1：
# 输入：m = 2, n = 3, k = 1
# 输出：3
# 示例 2：
# 输入：m = 3, n = 1, k = 0
# 输出：1
# 提示：

#这题关键的是有个visit=set（）  无重复的集合
from jz14 import fuc

def sums(n):
        ans = 0
        while n:
            ans += n % 10   #求余
            n //= 10        #左移
        return ans          #一个坐标的各个位数和

def dfs(arr,i,j,k)

    res = dfs(i+1,j,k) or dfs(i-1,j,k) or dfs(i,j+1,k) or dfs(i,j-1,k)
    k


def dfs(i, j, si, sj):#深度优先搜索 si,sj 都是0 在return进行累加
    if i >= m or j >= n or k < si + sj or (i, j) in visited: return 0  #判断边界值以及是否小于k ，超过则返回0，还要判断是否这个坐标扫描过
    visited.add((i, j))
    return 1 + dfs(i + 1, j, si + 1 if (i + 1) % 10 else si - 8,
                   sj) + dfs(i, j + 1, si,
                             sj + 1 if (j + 1) % 10 else sj - 8)#向下向右扫描

def bfs(m,n,k):#广度优先搜索
    queue, visited = [(0, 0, 0, 0)], set()   #queue里四个数对应i，j ，si,sj
    while queue:
        i, j, si, sj = queue.pop(0)
        if i >= m or j >= n or k < si + sj or (i, j) in visited: continue  #和dfs一样判断边界 以及判断是否拜访过 越界或者拜访过就下一个
        visited.add((i, j))
        queue.append((i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj))#队列里增加 右和下两个位置的坐标
        queue.append((i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8))
    return len(visited)
#直到队列空
visited = set()#建立一个无重复的集合
return dfs(0, 0, 0, 0)





