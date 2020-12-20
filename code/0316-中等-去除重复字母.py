def removeDuplicateLetters(s):
    # 记录剩余字符数量
    char_counter = dict()
    for char in s:
        if char in char_counter:
            char_counter[char] += 1
        else:
            char_counter[char] = 1
    # 记录已经在栈中的那些字符
    char_in_stack = {char:0 for char in char_counter}
    # 单调栈：底→顶
    stack = []
    for char in s:
        char_counter[char] -= 1
        # 如果待添字符已经在栈中了，则放弃
        if char_in_stack[char] == 1:
            continue
        # 否则，执行连续弹出，直到：①栈为空 or ②栈顶元素不能再弹了不然没了 or ③栈顶元素小于待添元素
        while (len(stack)>0) and (char_counter[stack[-1]]>0) and (stack[-1]>char):
            tmp = stack.pop()
            # 这里不需要再char_counter[char] -= 1，因为入栈就已经耗掉了
            char_in_stack[tmp] = 0
        stack.append(char)
        char_in_stack[char] = 1
    return "".join(stack)