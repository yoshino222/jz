# 从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        ans, que = [], collections.deque()
        que.append(root)
        while que:
            tmp = []
            for _ in range(len(que)):
                node = que.popleft()
                tmp.append(node.val)
                if node.left: que.append(node.left)
                if node.right: que.append((node.right))
            ans.append(tmp)
        return ans

