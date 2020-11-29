class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2):
    ################# 递归做法 #################
    # 基本结束条件
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    # 缩小问题规模 & 调用自身
    if l1.val < l2.val:
        node = ListNode(l1.val)
        l1   = l1.next
        node.next = mergeTwoLists(l1,l2)
        return node
    else:
        node = ListNode(l2.val)
        l2   = l2.next
        node.next = mergeTwoLists(l1,l2)
        return node 
    ################# 非递归做法 #################
    # if l1 is None:
    #     return l2
    # if l2 is None:
    #     return l1
    # head = None
    # tail = None
    # while l1 and l2:
    #     if l1.val < l2.val:
    #         tmp_val = l1.val
    #         l1 = l1.next
    #     else:
    #         tmp_val = l2.val
    #         l2 = l2.next
    #     if head is None:
    #         head = ListNode(tmp_val)
    #         tail = head
    #     else:
    #         tail.next = ListNode(tmp_val)
    #         tail = tail.next
    # # 可能剩下某个链表还有值，接到tail之后
    # if l1:
    #     tail.next = l1
    # elif l2:
    #     tail.next = l2
    # return head


if __name__ == "__main__":
    ############# Test sample #############
    l1           = ListNode(1)
    l1.next      = ListNode(2)
    l1.next.next = ListNode(4)
    l2           = ListNode(1)
    l2.next      = ListNode(3)
    l2.next.next = ListNode(4)
    #######################################
    res = mergeTwoLists(l1, l2)

    while res:
        print(res.val)
        res = res.next


