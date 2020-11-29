class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    curr_l1  = l1
    curr_l2  = l2
    ans_head = ListNode(-999)
    ans_curr = ans_head

    # 进位计数器
    carry = 0
    while curr_l1 or curr_l2:
        tmp = carry
        if curr_l1:
            tmp += curr_l1.val
            curr_l1  = curr_l1.next
        if curr_l2:
            tmp += curr_l2.val
            curr_l2  = curr_l2.next
        if tmp >= 10:
            carry = tmp//10
            tmp   = tmp%10
        else:
            # 特别注意如果某位相加不进位的话，计数器要清零
            carry = 0
        ans_curr.next = ListNode(tmp)
        ans_curr = ans_curr.next
    
    # 最后一位完，如果还有进位，其实就是在最前补个1
    if carry != 0:
        ans_curr.next = ListNode(carry)
    
    return ans_head.next
        
# [9,9,9,9,9,9,9]
# [9,9,9,9]


