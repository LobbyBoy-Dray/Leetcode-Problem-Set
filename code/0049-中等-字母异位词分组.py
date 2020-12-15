def groupAnagrams(strs):
    # 字母排序作为哈希表的键
    my_dict = dict()
    for word in strs:
        sorted_word = "".join(sorted(word))
        if sorted_word in my_dict:
            my_dict[sorted_word].append(word)
        else:
            my_dict[sorted_word] = [word]
    res = [my_dict[i] for i in my_dict]
    return res