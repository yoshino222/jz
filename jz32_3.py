# 请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        ans, que = [], collections.deque()
        que.append(root)
        carry=1
        while que:
            tmp = []
            for _ in range(len(que)):
                node = que.popleft()#if len(ans)%2:tmp.appendleft(node.val)  双端队列
                tmp.append(node.val)
                if node.left: que.append(node.left)
                if node.right: que.append((node.right))
            if carry==1:
                ans.append(tmp)
                carry=0
            else:
                ans.append(tmp[::-1])
                carry=1
        return ans