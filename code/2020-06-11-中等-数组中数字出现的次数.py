# 一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。
# 请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。

# 异或：
# 交换率：p XOR q = q XOR p
# 结合率：p XOR (q XOR r) = (p XOR q) XOR r
# p XOR 0 = p
# p XOR q XOR q = p

def singleNumbers(nums):
    result = []
    # 先做一遍异或，得到那两个目标数字异或的结果
    xorResult = 0
    for i in nums:
        xorResult = xorResult ^ i
    # 分组
    h = 1
    while(xorResult & h == 0):
        h <<= 1
    return h

nums = [7,4,1,4]
print(singleNumbers(nums))