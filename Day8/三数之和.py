def threeSum(nums):
    nums.sort()
    res = []
    hashset = set()
    
    for i in range(len(nums)):
        if nums[i] > 0:
            break
        tple = findTuple(i,nums)
        if tple and tuple(tple) not in hashset:
            hashset.add(tuple(tple))
            res.append([nums[i],tple[0],tple[1]])
    
    return res

def findTuple(i,arr):
    left,right = i+1,len(arr)-1
    
    while left < right:
        if arr[i] + arr[left] + arr[right] == 0:
            return [arr[left],arr[right]]
        elif arr[i] + arr[left] + arr[right] < 0:
            left += 1
        else:
            right -= 1
    
    return []

print(threeSum([-1,0,1,2,-1,-4]))

