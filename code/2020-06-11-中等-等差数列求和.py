# 求 1+2+...+n 
# 要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）
# Python中的and和or：返回它最后check到的那个操作数——注意短路特性

def toSum(n):
    return n and (n + toSum(n-1))

print(toSum(3))
print(toSum(9))