# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head):
        # ############## 递归解法 ##############
        # self.counter  = 0
        # self.counter2 = 0
        # self.ans_node = None

        # def go(node):
        #     if node is None:
        #         return None
        #     self.counter += 1
        #     go(node.next)
        #     self.counter2 += 1
        #     tmp = self.counter//2 if self.counter%2==0 else (self.counter//2+1)
        #     if self.counter2 == tmp:
        #         self.ans_node = node
        
        # go(head)

        # return self.ans_node
        
        ############## 非递归解法-双指针 ##############
        fast = head
        slow = head
        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next
        return slow





if __name__ == "__main__":
    pass