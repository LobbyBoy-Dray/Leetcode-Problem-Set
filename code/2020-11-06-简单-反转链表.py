class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def print_linklist(linklist):
    while linklist:
        print(linklist.val)
        linklist = linklist.next

def construct_linklist(mylist):
    head    = ListNode(-999)
    current = head
    for i in mylist:
        current.next = ListNode(i)
        current = current.next
    return head.next



def reverseList(head):
    # # 法一：迭代法
    # #     - prev和curr两个指针
    # #     - 先用tmp暂存curr的next——这样就可以放心该curr的指向了
    # #     - 将curr的指向改为其前一个——反转
    # #     - 移动prev和curr指针
    # prev = None
    # curr = head
    # while curr:
    #     tmp_next  = curr.next
    #     curr.next = prev
    #     prev      = curr
    #     curr      = tmp_next
    # return prev

    # 法二：递归法
    if (head is None) or (head.next is None):
        return head
    tmp = reverseList(head.next)
    # 为什么两个next？
    # head.next，指向的是原来第二个node，虽然现在第二个node已经变成新的链表的最后一个了
    # head.next.next就指向的是反转链表的最后一个node的指向，本来是None，现在把head赋给它
    # 但别忘了head的next要设为None，因为现在它是最后一个了
    head.next.next = head
    head.next = None
    return tmp

if __name__ == "__main__":
    linklist = construct_linklist([2,1,3,3,3,4])
    linklist = reverseList(linklist)
    print_linklist(linklist)