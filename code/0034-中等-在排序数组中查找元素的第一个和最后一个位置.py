def searchRange(nums, target):
    # # 12.54%，29.72%
    # def find_left_or_right(nums, target, direction):
    #     idx      = None
    #     start    = 0
    #     end      = len(nums)-1
    #     while start<= end:
    #         mid = (start+end)//2
    #         if nums[mid] == target:
    #             idx = mid
    #             if direction == "l":
    #                 end = mid-1
    #             elif direction == "r":
    #                 start = mid+1
    #             else:
    #                 raise Exception
    #         elif nums[mid] > target:
    #             end = mid-1
    #         else:
    #             start = mid+1
    #     return idx
    # tmp1 = find_left_or_right(nums, target, "l")
    # tmp1 = -1 if tmp1 is None else tmp1
    # tmp2 = find_left_or_right(nums, target, "r")
    # tmp2 = -1 if tmp2 is None else tmp2
    # return [tmp1, tmp2]

    # 89.49%，26.63%
    ################### 辅助函数 ###################
    def find_left_or_right(nums, target, direction):
        idx      = None
        start    = 0
        end      = len(nums)-1
        while start<= end:
            mid = (start+end)//2
            if nums[mid] == target:
                idx = mid
                if direction == "l":
                    end = mid-1
                elif direction == "r":
                    start = mid+1
                else:
                    raise Exception
            elif nums[mid] > target:
                end = mid-1
            else:
                start = mid+1
        return idx
    ################### 主函数 ###################
    left_idx  = None
    right_idx = None
    start     = 0
    end       = len(nums)-1
    while start<=end:
        mid = (start+end)//2
        if nums[mid]==target:
            left_idx  = find_left_or_right(nums[:mid+1], target, "l")
            # 这里一定要加上mid！
            right_idx = find_left_or_right(nums[mid:], target, "r") + mid
            break
        elif nums[mid]>target:
            end = mid-1
        else:
            start = mid+1
    left_idx  = -1 if left_idx is None else left_idx
    right_idx = -1 if right_idx is None else right_idx
    return [left_idx, right_idx]