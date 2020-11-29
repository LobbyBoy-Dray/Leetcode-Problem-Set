# 输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。
# 假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def buildTreeHelper(preorder, inorder):
    """
    input:
        - preorder  : List[int]
        - inorder   : List[int]
    output:
        - TreeNode
    """
    # 基本结束条件 - 为空，返回None
    if len(preorder) == 0:
        return None
    # preorder的第一个值是根节点
    rootVal             = preorder[0]
    # 找到该值在inorder中的位置，切出左子树的inorder和右子树的inorder
    rootValIndexInorder = inorder.index(rootVal)
    leftInorder         = inorder[:rootValIndexInorder]
    rightInorder        = inorder[rootValIndexInorder+1:]
    # 根据长度信息，切出左子树的preorder和右子树的preorder
    leftPreorder        = preorder[1:1+len(leftInorder)]
    rightPreorder       = preorder[1+len(leftInorder):]
    # 递归构建左子树和右子树
    leftTree            = buildTreeHelper(leftPreorder, leftInorder)
    rightTree           = buildTreeHelper(rightPreorder, rightInorder)
    # 合并
    root                = TreeNode(rootVal)
    root.left           = leftTree
    root.right          = rightTree
    return root

def buildTree(preorder, inorder):
    if len(preorder) == 0:
        return None
    else:
        return buildTreeHelper(preorder, inorder)

preorder = [3,9,20,15,7]
inorder  = [9,3,15,20,7]
