# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root):
        if root is None:
            return 0
        # 树的高度
        height = 0
        temp_node = root
        while temp_node.left is not None:
            height += 1
            temp_node = temp_node.left
        # 深度优先遍历
        stop = False
        counter = 0
        def dfs(node, level, height):
            nonlocal stop
            nonlocal counter
            if not stop:
                # 既无左子，也无右子
                if node.left is None and node.right is None:
                    # 情况1：最底层的叶结点
                    if level == height:
                        counter += 1
                    # 情况2：倒数第二层的叶结点——停止递归
                    else:
                        stop = True
                # 无右子
                elif node.right is None:
                    # 把其左子算上后停止递归
                    counter += 1
                    stop = True
                # 继续递归
                else:
                    dfs(node.left, level+1, height)
                    dfs(node.right, level+1, height)
            else:
                return None
        dfs(root, 0, height)
        total_nodes = 2 ** height -1 + counter
        return total_nodes