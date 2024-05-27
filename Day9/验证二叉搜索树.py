# 给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。
# 有效二叉搜索树定义如下：
# 节点的左子树只包含 小于 当前节点的数。
# 节点的右子树只包含 大于 当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root):
    if root is None:
        return False
    min_value, max_value = float("-inf"), float("inf")

    return dfs(root, min_value, max_value)


def dfs(root, min_value, max_value):
    if root is None:
        return True

    if not (min_value < root.val < max_value):
        return False

    return dfs(root.left, min_value, root.val) and dfs(root.right, root.val, max_value)


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.right.left = TreeNode(6)
root.right.right = TreeNode(20)

print(isValidBST(root))
