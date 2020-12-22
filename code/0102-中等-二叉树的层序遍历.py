# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        # ############ 解法一：配合队列进行BFS ############
        # # 尾 → 头
        # queue = [(root,0)]
        # result     = []
        # group      = []
        # curr_level = 0
        # while queue:
        #     node = queue.pop()
        #     if node[1] == curr_level:
        #         group.append(node[0].val)
        #     else:
        #         result.append(group)
        #         curr_level = node[1]
        #         group      = [node[0].val]
        #     if node[0].left:
        #         queue.insert(0, (node[0].left, curr_level+1))
        #     if node[0].right:
        #         queue.insert(0, (node[0].right, curr_level+1))
        # result.append(group)
        # return result
        ############ 解法二：对上一种解法的空间上的优化 ############
        result = []
        queue  = [root]
        while queue:
            result.append([node.val for node in queue])
            tmp_queue = []
            for node in queue:
                if node.left:
                    tmp_queue.append(node.left)
                if node.right:
                    tmp_queue.append(node.right)
            queue = tmp_queue
        return result