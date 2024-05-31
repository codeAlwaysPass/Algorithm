def minDepth(root):
    if root is None:
        return 0

    left = minDepth(root.left)
    right = minDepth(root.right)

    if not left or not right:
        return left if left else right

    return min(left, right) + 1
