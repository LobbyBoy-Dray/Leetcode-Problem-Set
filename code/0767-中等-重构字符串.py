def reorganizeString(S):
    S = "".join(sorted(S))
    max_alpha = None
    max_count = -1
    for i in set(S):
        if S.count(i) > max_count:
            max_count = S.count(i)
            max_alpha = i
    
    # 失败，不能构建目标字符串
    if len(S) < (2*max_count-1):
        return ""
    # 成功，构建目标字符串
    res = max_alpha * max_count
    S   = S.replace(max_alpha, "")

    tmp = ""
    while S:
        tmp += (res[0]+S[0])
        res = res[1:]
        S   = S[1:]
        if res == "":
            res = tmp
            tmp = ""
    
    return tmp+res

if __name__ == "__main__":
    S1 = "aaab"
    S2 = "aab"
    print(reorganizeString(S1))
    print(reorganizeString(S2))