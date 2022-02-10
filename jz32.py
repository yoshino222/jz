#从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。

# 例如:
# 给定二叉树: [3,9,20,null,null,15,7],
# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root) :
        if not root:return []
        ans,que=[],collections.deque()
        que.append(root)
        while que:
            node=que.popleft()
            ans.append(node.val)
            if node.left:que.append(node.left)
            if node.right:que.append(node.right)
        return ans






# [3,9,20,null,null,15,7],
# s=Solution()
# print(s.levelOrder(a))
