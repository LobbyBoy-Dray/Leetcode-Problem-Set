# 请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
# 路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。
# 如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。
# 例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。
# [["a","b","c","e"],
# ["s","f","c","s"],
# ["a","d","e","e"]]
# 但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。


def exist(board, word):
    # ===================== 全局变量 =====================
    rowNum = len(board)
    colNum = len(board[0])
    done   = []
    # ====================================================
    # 判断有没有当前位置是否有效：出界？已经走过？
    def isValid(x, y):
        if ((x,y) in done) or (x < 0) or (x > rowNum-1) or (y < 0) or (y > colNum-1):
            return False
        else:
            return True
    # 计算四周可行的坐标
    def nextPosition(x, y):
        candidates = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
        result     = []
        for i in candidates:
            if isValid(i[0], i[1]):
                result.append(i)
        return result
    # 递归函数
    def hepler(currentPos, reaminWord):
        if reaminWord == '':                                        # 剩余单词为空，则说明完成一条路径
            return True
        elif nextPosition(currentPos[0],currentPos[1]) == []:       # 剩余单词不为空，但是已经无路可走了
            done.pop()                                              # 弹出该位置——回溯
            return False
        else:
            nextStep = nextPosition(currentPos[0],currentPos[1])
            for n in nextStep:
                if reaminWord[0] == board[n[0]][n[1]]:              # 若下一步的位置的字母 = 单词的第一个字母，递归
                    done.append(n)                                  
                    tmp = hepler(n, reaminWord[1:])
                    if tmp == True:
                        return True
            done.pop()
            return False
    # =========================================================
    for row in range(rowNum):
        for col in range(colNum):
            if word[0] == board[row][col]:
                result = hepler((row,col), word[1:])
                if result == True:
                    return True
    return False

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(exist(board, word))