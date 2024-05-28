def myPow(x, n):
    if x == 0.0:
        return 0.0

    res = 1

    while n:
        # n & 1等价于取n % 2
        if n & 1:
            res *= x

        # x直接变为x^2
        x *= x
        # n // 2
        n >>= 1

    return res


# 时间复杂度为O(lgn)
