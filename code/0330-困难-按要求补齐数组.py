def minPatches(nums, n):
    max_cover = 0
    counter   = 0
    nums      = nums + [n+1]
    for num in nums:
        while num > (max_cover+1):
            counter += 1                    # 添加max_cover+1
            max_cover = 2*max_cover+1       # 更新max_cover
            if max_cover >= n:
                return counter
        else:
            max_cover += num
            if max_cover >= n:
                return counter
    return counter