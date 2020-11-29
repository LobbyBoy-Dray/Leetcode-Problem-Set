# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。
# 如果是则返回 true，否则返回 false。
# 假设输入的数组的任意两个数字都互不相同。

# 思路：
# 一棵树的后序遍历：[左子树部分   右子树部分   根]
# 递归

def verifyPostorder(postorder):
    if len(postorder) <= 1:
        return True
    root = postorder.pop()                      
    for index in range(len(postorder)+1):       # +1很重要
        leftPostorderList  = postorder[:index]
        rightpostorderList = postorder[index:]
        if leftPostorderList == []:
            if (root <= min(rightpostorderList)) and verifyPostorder(rightpostorderList):
                return True
            else:
                continue
        if rightpostorderList == []:
            if (root >= max(leftPostorderList)) and verifyPostorder(leftPostorderList):
                return True
            else:
                continue     
        if (root >= max(leftPostorderList)) and (root <= min(rightpostorderList)):
            if verifyPostorder(leftPostorderList) and verifyPostorder(rightpostorderList):
                return True
            else:
                continue
    return False

postorderList1 = [1,6,3,2,5]            # 输出：False
postorderList2 = [1,3,2,6,5]            # 输出：True
postorderList3 = [4, 6, 7, 5]           # 输出：True
print(verifyPostorder(postorderList1))
print(verifyPostorder(postorderList2))
print(verifyPostorder(postorderList3))

