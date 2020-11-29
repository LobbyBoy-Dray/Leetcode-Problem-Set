# 在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。
# 你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。
# 给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？
# 思路：动态规划
# 
#                 |
#               X |
#             X O |
#            —— ——



def maxValue(grid):
    rowNum = len(grid)
    colNum = len(grid[0])
    result = [[None]*colNum]*rowNum
    for row in range(rowNum):
        for col in range(colNum):
            if row == 0:                                            # 棋盘只有1行
                result[row][col] = sum(grid[0][:col+1])
                continue
            if col == 0:
                result[row][col] = sum([r[0] for r in grid[:row+1]]) # 棋盘只有1列
                continue
            upMax   = result[row-1][col]
            leftMax = result[row][col-1]
            tmpMax  = (upMax + grid[row][col]) if upMax > leftMax else (leftMax + grid[row][col])
            result[row][col] = tmpMax
    return result[rowNum-1][colNum-1]

grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
print(maxValue(grid))