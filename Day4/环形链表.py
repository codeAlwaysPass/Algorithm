class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head):
    if head is None:
        return False
    
    slow,fast = head,head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    
    return False

def arrayToListNode(array):
    if not array:
        return None
    head = ListNode(array[0])
    current = head
    for value in array[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# 辅助函数：打印链表
def printListNode(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    print("->".join(map(str, values)))

# 构造链表数组
array = [1, 2, 3, 4, 5]
head = arrayToListNode(array)
print(hasCycle(head))