# 给定一个大小为 n 的数组 nums ，返回其中的多数元素。
# 多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
from collections import defaultdict


def majorityElement(nums):
    hashmap = defaultdict(0)

    for num in nums:
        hashmap[num] += 1
        if hashmap[num] > len(nums) // 2:
            return num

    return None


# 该算法还有更优解, 投票算法
