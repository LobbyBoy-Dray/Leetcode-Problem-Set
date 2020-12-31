def eraseOverlapIntervals(intervals):
    intervals.sort(key=lambda x:x[1])
    counter    = 0
    target_pos = 0
    for idx in range(1, len(intervals)):
        # curr的左边界小于target的右边界，那么curr必须删掉——因为curr和target必删一个，删哪个？肯定删右边界小的
        if intervals[idx][0] < intervals[target_pos][1]:
            counter += 1
            continue
        else:
            target_pos = idx
    return counter