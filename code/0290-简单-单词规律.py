def wordPattern(pattern, s):
    pattern_list = list(pattern)
    str_list     = s.split(" ")
    if len(pattern_list) != len(str_list):
        return False
    # 
    map_from_pattern_to_str = dict()
    map_from_str_to_pattern = dict()
    #
    idx = 0
    while idx < len(pattern_list):
        from_pattern = pattern_list[idx] in map_from_pattern_to_str
        from_string  = str_list[idx] in map_from_str_to_pattern
        if from_pattern and from_string:
            tmp1 = map_from_pattern_to_str[pattern_list[idx]] != str_list[idx]
            tmp2 = map_from_str_to_pattern[str_list[idx]]     != pattern_list[idx]
            if tmp1 or tmp2:
                return False
            else:
                idx += 1
        elif (not from_pattern) and (not from_string):
            map_from_pattern_to_str[pattern_list[idx]] = str_list[idx]
            map_from_str_to_pattern[str_list[idx]]     = pattern_list[idx]
            idx += 1
        else:
            return False
    return True