class RobotMovement:
    def __init__(self, m, n, k):
        self.m = m
        self.n = n
        self.k = k
    
    def computeDigitSum(self, x, y):
        totalSum = 0
        for i in str(x)+str(y):
            totalSum += int(i)
        return totalSum

    def isValid(self, x, y):
        if (x < 0) or (y < 0) or (x > self.m-1) or (y > self.n-1):
            return False
        elif self.computeDigitSum(x,y) > self.k:
            return False
        else:
            return True
    
    def solution1(self):
        """
        队列
        """
        totalCount = 0                  # 记录可行格子数量
        toQueue    = []                 # 待检查的格子的队列
        doneList   = []                 # 已经检查过的格子的列表
        toQueue.insert(0, (0,0))        # 原点入队
        while len(toQueue) > 0:
            thisLoc = toQueue.pop()
            if thisLoc in doneList:
                continue
            else:
                doneList.append(thisLoc)
                if self.isValid(thisLoc[0], thisLoc[1]):
                    totalCount += 1
                    toQueue.insert(0, (thisLoc[0]-1,thisLoc[1]))
                    toQueue.insert(0, (thisLoc[0]+1,thisLoc[1]))
                    toQueue.insert(0, (thisLoc[0],thisLoc[1]-1))
                    toQueue.insert(0, (thisLoc[0],thisLoc[1]+1))
                else:
                    continue
        return totalCount

    def solution2(self):
        """
        深度优先搜索
        """
        self.dfsTimes = 0
        doneList      = []
        offsets       = [[-1,0],[+1,0],[0,-1],[0,+1]]
        def visit(x ,y):
            doneList.append((x,y))
            if self.isValid(x,y):
                self.dfsTimes += 1
                for offset in offsets:
                    newX = x + offset[0]
                    newY = y + offset[1]
                    if self.isValid(newX, newY) and (newX, newY) not in doneList:
                        visit(newX, newY)
        visit(0,0)
        return self.dfsTimes



rm = RobotMovement(3,1,0)
print(rm.solution1())
print(rm.solution2())