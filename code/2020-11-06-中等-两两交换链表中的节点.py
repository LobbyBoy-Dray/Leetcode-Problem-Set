class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head):
    # 先固定真实开头
    before = head
    # 添加哑结点
    tmp      = ListNode(-999)
    tmp.next = head
    head     = tmp
    # 前驱设置
    previous = head
    while before and before.next:
        after        = before.next

        tmp           = after.next
        previous.next = after
        after.next    = before
        before.next   = tmp

        previous = before

        before = before.next
    # 去掉哑结点
    head = head.next
    return head

    # if (head is None) or (head.next) is None:
    #     return head
    # first       = head
    # second      = head.next
    # stop        = False
    # previous    = None
    # new_head    = second

    # while not stop:
    #     remain = second.next
    #     if previous is not None:
    #         previous.next = second
    #     second.next = first
    #     first.next  = remain

    #     if (remain is None) or (remain.next is None):
    #         stop = True
    #     else:
    #         previous = first
    #         first    = first.next
    #         second   = first.next
    # return new_head