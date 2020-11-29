# 输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。
# 给定二叉树 [3,9,20,null,null,15,7]
# 返回它的最大深度3
# 这里根节点未第1层

class TreeNode:
    def __init__(self, x):
        self.val   = x
        self.left  = None
        self.right = None

# 深度优先的方法
class SolutionDFS: 
    def dfs(self, rootNode, level, leafDepthList):
        if rootNode.left == None and rootNode.right == None:
            leafDepthList.append(level)
        else:
            if rootNode.left != None:
                self.dfs(rootNode.left, level+1, leafDepthList)
            if rootNode.right != None:
                self.dfs(rootNode.right, level+1, leafDepthList)

    def maxDepth(self, root):
        if root == None:
            return 0
        else:
            leafDepthList = []
            self.dfs(root, 1, leafDepthList)
            return (max(leafDepthList))

# 广度优先的方法
class SolutionBFS:
    def maxDepth(self, rootNode):
        if rootNode == None:
            return 0
        else:
            maxLevel = -1
            myStack  = [(rootNode, 1)]          # 节点队列
            while len(myStack) != 0:
                currentNode, currentDepth = myStack.pop(0)
                if currentDepth > maxLevel:
                    maxLevel = currentDepth
                if currentNode.left != None:
                    myStack.append((currentNode.left, currentDepth+1))
                if currentNode.right != None:
                    myStack.append((currentNode.right, currentDepth+1))
        return maxLevel

rootNode1             = None
rootNode2             = TreeNode(3)
rootNode2.left        = TreeNode(9)
rootNode2.right       = TreeNode(20)
rootNode2.right.left  = TreeNode(15)
rootNode2.right.right = TreeNode(7)

dfsSolver = SolutionDFS()
print(dfsSolver.maxDepth(rootNode1))
print(dfsSolver.maxDepth(rootNode2))
bfsSolver = SolutionBFS()
print(bfsSolver.maxDepth(rootNode1))
print(bfsSolver.maxDepth(rootNode2))
