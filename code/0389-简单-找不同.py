def findTheDifference(s, t):
    # ################## 解法一：哈希表计数 ##################
    # raw_dict      = dict()
    # modified_dict = dict()
    # for char in s:
    #     if char in raw_dict:
    #         raw_dict[char] += 1
    #     else:
    #         raw_dict[char] = 1
    # for char in t:
    #     if char in modified_dict:
    #         modified_dict[char] += 1
    #     else:
    #         modified_dict[char] = 1
    # for key in modified_dict:
    #     if key not in raw_dict:
    #         return key
    #     elif modified_dict[key] > raw_dict[key]:
    #         return key
    ################## 解法二：位运算 ##################
    total = s+t
    tmp   = 0
    for char in total:
        tmp = tmp ^ ord(char)
    return chr(tmp)