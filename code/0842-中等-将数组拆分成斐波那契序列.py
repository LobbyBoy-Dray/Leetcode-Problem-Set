def splitIntoFibonacci(S):
    def helper(first_str, second_str, other_str):
        ######################
        if int(first_str) > (2**31-1):
            return False
        if int(second_str) > (2**31-1):
            return False            
        ########################
        if (first_str[0] == "0") and (first_str != "0"):
            return False
        ######################
        if other_str == "":
            return [int(first_str), int(second_str)]
        ######################
        first_num      = int(first_str)
        second_num     = int(second_str)
        goal_third_num = first_num+second_num
        goal_third_str = str(goal_third_num)
        goal_third_len = len(goal_third_str)

        if goal_third_str == other_str[:goal_third_len]:
            tmp = helper(second_str, goal_third_str, other_str[goal_third_len:])
            if tmp:
                return [int(first_str)] + tmp
            else:
                return False
        else:
            return False

    for len_1 in range(1, len(S)-1):
        for len_2 in range(1, len(S)-len_1):
            tmp = helper(S[:len_1], S[len_1:len_1+len_2], S[len_1+len_2:])
            if tmp:
                return tmp