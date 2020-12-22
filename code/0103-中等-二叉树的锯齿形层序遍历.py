# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        result    = []
        queue     = [root]
        from_left = True
        while queue:
            if from_left:
                result.append([node.val for node in queue])
            else:
                result.append([node.val for node in queue][::-1])
            tmp_queue = []
            for node in queue:
                if node.left:
                    tmp_queue.append(node.left)
                if node.right:
                    tmp_queue.append(node.right)
            queue     = tmp_queue
            from_left = not from_left
        return result