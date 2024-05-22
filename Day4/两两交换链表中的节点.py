class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head):
    # 创建一个虚拟头节点
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    
    while head and head.next:
        first_node = head
        second_node = head.next
        
        prev.next = second_node
        first_node.next = second_node.next
        second_node.next = first_node
        
        prev = first_node
        head = first_node.next
    
    return dummy.next


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

# 两两交换链表中的节点
swapped_head = swapPairs(head)
print("两两交换后的链表:")
printListNode(swapped_head)
