# 给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。

# 如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。

# 假设环境不允许存储 64 位整数（有符号或无符号）。


def reverse(num):
    minVal, maxVal = -(2**31), 2**31 - 1
    sign = -1 if num < 0 else 1
    num = abs(num)

    reversed_num = 0
    while num != 0:
        pop = num % 10
        num = num // 10

        if reversed_num > maxVal // 10 or (reversed_num == maxVal // 10 and pop > 7):
            return 0

        reversed_num = reversed_num * 10 + pop
    
    if sign * reversed_num < minVal:
        return 0

    return sign*reversed_num


num = 150
print(reverse(num))
