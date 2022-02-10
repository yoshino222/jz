# 请完成一个函数，输入一个二叉树，该函数输出它的镜像。
#
# 例如输入：
#
#
# 镜像输出：
#
#
# 示例 1：
#
# 输入：root = [4,2,7,1,3,6,9]
# 输出：[4,7,2,9,6,3,1]

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        def recur(root):
            if not root:
                return False
            root.right,root.left=root.left,root.right
        return  self.mirrorTree(root.right) and self.mirrorTreerecur(root.left)