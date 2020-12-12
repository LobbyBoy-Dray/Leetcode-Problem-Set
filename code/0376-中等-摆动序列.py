def wiggleMaxLength(nums):
    ################## 特殊情况：少于两个元素的序列也是摆动序列 ##################
    if len(nums) < 2:
        return len(nums)
    #############################################################################
    difference_list = []
    for i in range(1, len(nums)):
        difference_list.append(nums[i]-nums[i-1])
    
    tmp_list = []
    tmp      = 0
    for j in range(len(difference_list)):
        if tmp * difference_list[j] >= 0:
            tmp += difference_list[j]
        else:
            tmp_list.append(tmp)
            tmp = difference_list[j]
    tmp_list.append(tmp)

    if tmp_list == [0]:
        return 1
    else:
        return len(tmp_list)+1