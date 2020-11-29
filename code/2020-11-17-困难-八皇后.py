# 八皇后
# 打印N皇后在N×N棋盘上的各种摆法，其中每个皇后都不同行、不同列，也不在对角线上。
# 这里的“对角线”指的是所有的对角线，不只是平分整个棋盘的那两条对角线。

def solveNQueens(n):
    result = []
    def helper(board, curr_row):
        # 该函数不返回什么东西，是操作函数
        # board是棋盘，idx是棋盘的行，val是该行那一列有棋子
        # 在棋盘的curr_row行摆一个合适的棋子（base on之前的行都摆好）
        # 说明整个棋盘都摆完了
        if curr_row == len(board):
            result.append(board.copy())
        else:
            # 该行每一列都放一下，看行不行
            for col in range(len(board)):
                board[curr_row] = col
                success         = True
                # 看之前的行的摆放，会不会与该行的摆放矛盾
                for before_row in range(curr_row):
                    if (board[before_row] == board[curr_row]) or (abs(board[before_row]-board[curr_row]) == abs(before_row-curr_row)):
                        success = False
                        break
                # 没有任何矛盾，则摆下面一行
                if success:
                    helper(board, curr_row+1)
    init_board = [None] * n
    helper(init_board, 0)
    
    real_result = []
    for each_ans in result:
        real_result.append([("."*n)[:idx]+"Q"+("."*n)[idx+1:] for idx in each_ans])
    return len(real_result)

print(solveNQueens(15))













