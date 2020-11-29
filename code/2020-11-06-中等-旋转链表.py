class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotateRight(head, k):
    if head is None:
        return head
    deque = []
    while head:
        deque.append(head.val)
        head = head.next
    # k可能很大很大，但是这个不是real k——每轮len(deque)次，又回到原来的状态，所以实际上并不需要真的模拟k次
    k = k % len(deque)
    for _ in range(k):
        item = deque.pop()
        deque.insert(0,item)
    head = ListNode(deque.pop())
    while len(deque) != 0:
        tmp_val   = deque.pop()
        node      = ListNode(tmp_val)
        node.next = head
        head      = node
    return head

if __name__ == "__main__":
    ############# Test sample #############
    l1                     = ListNode(1)
    l1.next                = ListNode(2)
    l1.next.next           = ListNode(3)
    l1.next.next.next      = ListNode(4)
    l1.next.next.next.next = ListNode(5)
    #######################################
    rotateRight(l1, 2)