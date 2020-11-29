class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def partition(head, x):
    # 用哑结点初始化两个链表
    before_head = ListNode(-999)
    after_head  = ListNode(-999)
    # 指针初始化
    before      = before_head
    after       = after_head
    # 遍历原链表
    while head:
        if head.val < x:
            before.next = ListNode(head.val)
            before      = before.next
        else:
            after.next = ListNode(head.val)
            after      = after.next           
        head = head.next
    # 将before和after两个链表接起来，注意处理哑结点
    before.next = after_head.next
    before_head = before_head.next
    return before_head
    






    # # 不会用哑结点的憨批
    # new_head = None
    # new_tail = None
    # previous = None
    # current  = head
    # while current:
    #     if current.val < x:
    #         previous = current
    #         current  = current.next
    #     else:
    #         tmp     = current
    #         current = tmp.next
    #         if previous is None:
    #             head = current
    #         else:
    #             previous.next = tmp.next
    #         ###############
    #         tmp.next      = None
    #         if new_head is None:
    #             new_head = tmp
    #             new_tail = tmp
    #         else:
    #             new_tail.next = tmp
    #             new_tail      = tmp

    # if previous is None:
    #     return new_head
    # else:
    #     previous.next = new_head
    #     return head