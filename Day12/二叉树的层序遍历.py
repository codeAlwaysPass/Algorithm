from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root):
    if root is None:
        return []

    ans = []
    q = deque([root])

    while q:
        vals = []
        for _ in range(len(q)):
            node = q.popleft()
            vals.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        ans.append(vals)

    return ans
