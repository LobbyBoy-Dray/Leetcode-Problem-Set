# 从上到下打印出二叉树的每个节点
# 同一层的节点按照从左到右的顺序打印
# 广度优先搜索：BFS

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def levelOrder(root):
    if root == None:
        return []
    resultList = []
    nodeQueue  = []
    nodeQueue.insert(0,root)
    while len(nodeQueue) > 0:
        node = nodeQueue.pop()
        resultList.append(node.val)
        if node.left != None:
            nodeQueue.insert(0,node.left)
        if node.right != None:
            nodeQueue.insert(0,node.right)
    return resultList

tree1             = None
tree2             = TreeNode(3)
tree2.left        = TreeNode(9)
tree2.right       = TreeNode(20)
tree2.right.left  = TreeNode(15)
tree2.right.right = TreeNode(7)
print(levelOrder(tree1))
print(levelOrder(tree2))