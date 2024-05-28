# 因为是二叉搜索树,注意二叉搜索树的特性


def lowestCommonAncestor(root, p, q):
    # 当p,q都在左子树的情况
    if root.val > p.val and root.val > q.val:
        return lowestCommonAncestor(root.left, p, q)
    # 当p,q都在右子树的情况
    if root.val < p.val and root.val < q.val:
        return lowestCommonAncestor(root.right, p, q)

    # p,q分别在左右子树中,此时当前节点就是最近公共祖先
    return root
