class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
# 两个树，root的val一样
def isSubStructureForSameVal(rootFather, rootSon):
    """
        - input: 两个root.val相同的树——任何一个都不是None
        - output: True/False，即rootSon是否是rootFather的【同根子结构】
    """
    # condition1 - 左子树是不是【同根子结构】
    if rootSon.left != None:
        # 如果rootSon有左子树的话
        if (rootFather.left == None) or (rootFather.left.val != rootSon.left.val):
            # 若rootFather没有左子树或者两者左子树的val不一样，则rootSon与rootFather肯定不是【同根子结构】
            return False
        else:
            # 否则说明rootFather和rootSon左子树的root的val相同，那么递归得condition1
            condition1 = isSubStructureForSameVal(rootFather.left, rootSon.left)
    else:
        # 如果rootSon都没有左子树的话，肯定是
        condition1 = True
    # condition2 - 右子树是不是【同根子结构】
    if rootSon.right != None:
        if (rootFather.right == None) or (rootFather.right.val != rootSon.right.val):
            return False
        else:
            condition2 = isSubStructureForSameVal(rootFather.right, rootSon.right)
    else:
        condition2 = True
    # condition1和condition2需要同时成立
    if condition1 and condition2:
        return True
    else:
        return False

def isSubStructure(tree1, tree2):
    if (tree1 == None) or (tree2 == None):
        return False
    toExplore = [tree1]
    while len(toExplore) != 0:
        root = toExplore.pop()
        if root.val == tree2.val:
            result = isSubStructureForSameVal(root, tree2)
            if result:
                return True
        if root.left != None:
            toExplore.insert(0, root.left)
        if root.right != None:
            toExplore.insert(0, root.right)
    return False

# ===============================
tree1            = TreeNode(1)
tree1.left       = TreeNode(3)
tree1.right      = TreeNode(2)
tree1.left.left  = TreeNode(4)
tree2            = TreeNode(3)
tree2.left       = TreeNode(4)
# ===============================
print(isSubStructure(tree1, tree2))