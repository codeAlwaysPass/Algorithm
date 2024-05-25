# 给你一个整数数组 nums，
# 有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
# 返回 滑动窗口中的最大值 。
from collections import deque


def maxSlidingWindow(nums,k):
    ans = []
    #队列负责维护可能成为最大值的元素
    q = deque()
    
    for i,x in enumerate(nums):
        #如果队尾的数字比新加入的数字小, 那么它就一定不是最大值
        while q and nums[q[-1]] <= x:
            q.pop()
            
        #加入当前的数
        q.append(i)
        
        #如果队尾到当前数的距离大于滑窗长度, 那么队尾的元素要被踢出
        if i - q[0] >= k:
            q.popleft()
        
        #窗口满员时, 开始加入答案
        if i >= k - 1:
            ans.append(nums[q[0]])
    
    return ans
    
nums = [1,2,5,2,90,2121,31,-1]
print(maxSlidingWindow(nums,3))
    