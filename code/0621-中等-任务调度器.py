def leastInterval(tasks, n):
    # Step 1
    max_count = 0
    my_dict   = dict()
    for i in tasks:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1
        if my_dict[i] > max_count:
            max_count = my_dict[i]
    # Step 2
    max_nums  = []
    for i in my_dict:
        if my_dict[i] == max_count:
            max_nums.append(i)
    max_nums = len(max_nums)
    # Step 3
    if n < (max_nums - 1):
        return len(tasks)
    else:
        tmp = (max_count-1)*(n+1) + max_nums
        if tmp > len(tasks):
            return tmp
        else:
            return len(tasks)


if __name__ == "__main__":
    tasks = ["A","A","A","B","B","B","C","D","E","F","G"]
    n     = 2
    print(leastInterval(tasks, n))