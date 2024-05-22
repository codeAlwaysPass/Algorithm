#给定一个头节点为 head 的单链表用于记录一系列核心肌群训练编号，
# 请将该系列训练编号 倒序 记录于链表并返回。
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def listNodeReverse(head):
    if head is None:
        return None
    
    prev,next = None,None
    
    while head:
        next = head.next
        head.next = prev
        
        prev = head
        head = next

    return prev


    # 辅助函数：将数组转换为链表
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
print("原始链表:")
printListNode(head)

# 反转链表
reversed_head = listNodeReverse(head)
print("反转后的链表:")
printListNode(reversed_head)
