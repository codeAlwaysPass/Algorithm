def sort(arr):
    if len(arr) <= 1:
        return arr
    left, right = 0, len(arr) - 1
    quick_sort(left, right, arr)

    return arr


def quick_sort(left, right, arr):
    if left >= right:
        return

    pivot = getPivot(left, right, arr)
    #这里千万别把pivot重新包括进来
    quick_sort(left, pivot-1, arr)
    quick_sort(pivot+1, right, arr)


def getPivot(left, right, arr):
    pivot = left
    index = pivot + 1

    for i in range(index, right + 1):
        if arr[i] < arr[pivot]:
            arr[i], arr[index] = arr[index], arr[i]
            index += 1
            
    arr[pivot],arr[index-1] = arr[index-1],arr[pivot]
    pivot = index - 1

    return pivot

arr = [3,5,9,8,2,1,0,3,-1,-912]

print(sort(arr))