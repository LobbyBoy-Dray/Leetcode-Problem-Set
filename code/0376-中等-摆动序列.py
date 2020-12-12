def wiggleMaxLength(nums):
    ################## 特殊情况：少于两个元素的序列也是摆动序列 ##################
    if len(nums) < 2:
        return len(nums)
    #############################################################################
    difference_list = []
    for i in range(1, len(nums)):
        difference_list.append(nums[i]-nums[i-1])
    #############################################################################
    counter   = 0
    prev_sign = 0
    for i in difference_list:        
        if i == 0:
            continue
        curr_sign = 1 if i > 0 else -1
        if prev_sign != curr_sign:
            counter   += 1
            prev_sign = curr_sign
    return counter+1