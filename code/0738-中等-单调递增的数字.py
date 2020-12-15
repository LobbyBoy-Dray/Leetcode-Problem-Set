def monotoneIncreasingDigits(N):
    # 遍历，找到第一个与最高位X不一样的Y（找不到的话说明该数所有数字一样，返回即可）：
    #     - X > Y：最高位-1，其他位莽9即可；
    #     - X < Y：规模更小子问题（去除前面重复的那一串）

    # 将数字拆成数组
    num_list = [int(i) for i in list(str(N))]
    # 递归函数
    def helper(num_list):
        highest_digit   = num_list[0]
        found_different = False
        for i in range(1, len(num_list)):
            if num_list[i] != highest_digit:
                found_different = True
                idx_different   = i
                break
        # num_list中所有数字都一样
        if not found_different:
            return num_list
        # 找到了那个不一样的数字
        if highest_digit > num_list[idx_different]:
            res = ([highest_digit-1] + [9]*(len(num_list)-1)) if highest_digit != 1 else [9]*(len(num_list)-1)
            return res
        else:
            part1 = num_list[:idx_different]
            part2 = helper(num_list[idx_different:])
            return part1+part2
    # 调用递归
    res = helper(num_list)
    res = int("".join([str(i) for i in res]))
    return res