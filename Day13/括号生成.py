# 数字 n 代表生成括号的对数，
# 请你设计一个函数，用于能够生成所有可能的并且有效的括号组合。


def generateParenthesis(n):
    m = n * 2
    ans = []
    path = [""] * m

    def dfs(i, open):
        # 括号数量全部用完
        if i == m:
            ans.append("".join(path))
            return
        # 左括号没用完
        if open < n:
            path[i] = "("
            dfs(i + 1, open + 1)
        # 右括号数量不能小于左括号数量
        if i - open < open:
            path[i] = ")"
            dfs(i + 1, open)

    dfs(0, 0)
    return ans
