# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
# 百度百科中最近公共祖先的定义为：
# “对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，
# 满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”


def lowestCommonAncestor(root, p, q):
    # 如果当前节点是p或q, 最近公共祖先就是它自己
    if not root or (root == p or root == q):
        return root

    # 向左右子树寻找p,q节点 (左右子树不可能同时包含p,q两个节点)
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    # 都在右子树的情况
    if not left:
        return right
    # 都在左子树的情况
    if not right:
        return left

    # 如果左右子树都存在,说明p,q一个分别在左右子树中, 直接返回当前节点
    # 当前节点就是最近公共祖先
    return root
