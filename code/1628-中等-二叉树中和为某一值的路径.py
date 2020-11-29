class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root, givenSum):
        if root == None:
            return []
        else:
            resultList = []
            self.dfs(root, [], 0, givenSum, resultList)
            return resultList

    def dfs(self, root, tmpNodeList, accuSum, totalSum, resultList):
        tmpNodeList.append(root.val)
        accuSum += root.val
        if root.left == None and root.right == None:
            if accuSum == totalSum:
                resultList.append(tmpNodeList.copy())
        else:
            if root.left != None:
                self.dfs(root.left, tmpNodeList, accuSum, totalSum, resultList)
            if root.right != None:
                self.dfs(root.right, tmpNodeList, accuSum, totalSum, resultList)
        tmpNodeList.pop()


givenSum                    = 22
rootNode1                   = None
rootNode2                   = TreeNode(5)
rootNode2.left              = TreeNode(4)
rootNode2.right             = TreeNode(8)
rootNode2.left.left         = TreeNode(11)
rootNode2.left.left.left    = TreeNode(7)
rootNode2.left.left.right   = TreeNode(2)
rootNode2.right.left        = TreeNode(13)
rootNode2.right.right       = TreeNode(4)
rootNode2.right.right.left  = TreeNode(5)
rootNode2.right.right.right = TreeNode(1)
# ===========================================
sol = Solution()
print(sol.pathSum(rootNode1, givenSum))
print(sol.pathSum(rootNode2, givenSum))
