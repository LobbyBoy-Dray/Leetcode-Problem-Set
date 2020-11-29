class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def kthToLast(head, k):
    # ################# 非递归方法 #################
    # total_num = 0                           # 记录链表的总大小
    # my_dict   = dict()                      # 记录链表每个位置的val
    # curr      = head

    # while curr:
    #     total_num += 1
    #     my_dict[total_num] = curr.val
    #     curr = curr.next
    
    # return my_dict[total_num-k+1]           # 知道链表总大小和倒数第几，那就知道正数第几，直接访问dict即可

    # ################# 非递归方法-双指针 #################
    # fast = head
    # slow = head
    # while k != 0:
    #     fast = fast.next
    #     k -= 1
    # while fast:
    #     fast = fast.next
    #     slow = slow.next
    # return slow.val