def maxNumber(nums1, nums2, k):
    # def helper(nums, L):
#     # nums为非空数组，L<=len(nums)
#     # 从nums中挑出L个保持相对顺序的数字，使之表示的自然数最大
#     dp = []
#     for _ in range(len(nums)+1):
#         dp.append([None]*(L+1))
#     # l_0——数组前多少个——1~len(nums)
#     # l_1——目标长度——1~L
#     for l_0 in range(1, len(nums)+1):
#         for l_1 in range(1, L+1):
#             if l_0 < l_1:
#                 dp[l_0][l_1] = None
#             elif l_1 == 1:
#                 dp[l_0][l_1] = max(nums[:l_0])
#             elif l_0 == l_1:
#                 dp[l_0][l_1] = int("".join([str(i) for i in nums[:l_0]]))
#             else:
#                 tmp1 = dp[l_0-1][l_1]
#                 tmp2 = int(str(dp[l_0-1][l_1-1])+str(nums[l_0-1]))
#                 dp[l_0][l_1] = tmp1 if tmp1>tmp2 else tmp2
#     return [int(i) for i in list(str(dp[-1][-1]))]
    ##############################################
    def helper(nums, L):
        counter     = 0
        max_abandon = len(nums)-L
        stack       = []

        for idx in range(len(nums)):
            while (stack!=[]) and (counter<max_abandon) and (stack[-1]<nums[idx]):
                stack.pop()
                counter += 1
            stack.append(nums[idx])
        
        if counter < max_abandon:
            return stack[:(counter-max_abandon)]
        else:
            return stack
    ##############################################
    def is_former_bigger(nums1, nums2, idx1, idx2):
        while idx1<len(nums1) and idx2<len(nums2):
            if nums1[idx1] > nums2[idx2]:
                return True
            if nums1[idx1] < nums2[idx2]:
                return False
            idx1 += 1
            idx2 += 1
        if idx1 == len(nums1):
            return False
        return True

    def merge(nums1, nums2):
        if nums1 == []:
            return nums2
        if nums2 == []:
            return nums1
        
        merged = []
        idx1, idx2 = 0, 0
        while idx1<len(nums1) and idx2<len(nums2):
            if is_former_bigger(nums1, nums2, idx1, idx2):
                merged.append(nums1[idx1])
                idx1 += 1
            else:
                merged.append(nums2[idx2])
                idx2 += 1           
        if idx1 == len(nums1):
            merged.extend(nums2[idx2:])
        if idx2 == len(nums2):
            merged.extend(nums1[idx1:])
        
        return merged
    ##############################################
    result = [-1] * k
    for len_in_nums_1 in range(k+1):
        len_in_nums_2 = k - len_in_nums_1
        # 超过数组1的长度，不可能
        if len_in_nums_1 > len(nums1):
            break
        # 数组1需要负责更多的数字
        if len_in_nums_2 > len(nums2):
            continue
        # 正好
        tmp1 = helper(nums1, len_in_nums_1) if len_in_nums_1 != 0 else []
        tmp2 = helper(nums2, len_in_nums_2) if len_in_nums_2 != 0 else []
        tmp  = merge(tmp1, tmp2)
        if tmp > result:
            result = tmp
    return result


if __name__ == "__main__":
    nums1 = [8,9,7,3,5,9,1,0,8,5,3,0,9,2,7,4,8,9,8,1,0,2,0,2,7,2,3,5,4,7,4,1,4,0,1,4,2,1,3,1,5,3,9,3,9,0,1,7,0,6,1,8,5,6,6,5,0,4,7,2,9,2,2,7,6,2,9,2,3,5,7,4,7,0,1,8,3,6,6,3,0,8,5,3,0,3,7,3,0,9,8,5,1,9,5,0,7,9,6,8,5,1,9,6,5,8,2,3,7,1,0,1,4,3,4,4,2,4,0,8,4,6,5,5,7,6,9,0,8,4,6,1,6,7,2,0,1,1,8,2,6,4,0,5,5,2,6,1,6,4,7,1,7,2,2,9,8,9,1,0,5,5,9,7,7,8,8,3,3,8,9,3,7,5,3,6,1,0,1,0,9,3,7,8,4,0,3,5,8,1,0,5,7,2,8,4,9,5,6,8,1,1,8,7,3,2,3,4,8,7,9,9,7,8,5,2,2,7,1,9,1,5,5,1,3,5,9,0,5,2,9,4,2,8,7,3,9,4,7,4,8,7,5,0,9,9,7,9,3,8,0,9,5,3,0,0,3,0,4,9,0,9,1,6,0,2,0,5,2,2,6,0,0,9,6,3,4,1,2,0,8,3,6,6,9,0,2,1,6,9,2,4,9,0,8,3,9,0,5,4,5,4,6,1,2,5,2,2,1,7,3,8,1,1,6,8,8,1,8,5,6,1,3,0,1,3,5,6,5,0,6,4,2,8,6,0,3,7,9,5,5,9,8,0,4,8,6,0,8,6,6,1,6,2,7,1,0,2,2,4,0,0,0,4,6,5,5,4,0,1,5,8,3,2,0,9,7,6,2,6,9,9,9,7,1,4,6,2,8,2,5,3,4,5,2,4,4,4,7,2,2,5,3,2,8,2,2,4,9,8,0,9,8,7,6,2,6,7,5,4,7,5,1,0,5,7,8,7,7,8,9,7,0,3,7,7,4,7,2,0,4,1,1,9,1,7,5,0,5,6,6,1,0,6,9,4,2,8,0,5,1,9,8,4,0,3,1,2,4,2,1,8,9,5,9,6,5,3,1,8,9,0,9,8,3,0,9,4,1,1,6,0,5,9,0,8,3,7,8,5]
    nums2 = [7,8,4,1,9,4,2,6,5,2,1,2,8,9,3,9,9,5,4,4,2,9,2,0,5,9,4,2,1,7,2,5,1,2,0,0,5,3,1,1,7,2,3,3,2,8,2,0,1,4,5,1,0,0,7,7,9,6,3,8,0,1,5,8,3,2,3,6,4,2,6,3,6,7,6,6,9,5,4,3,2,7,6,3,1,8,7,5,7,8,1,6,0,7,3,0,4,4,4,9,6,3,1,0,3,7,3,6,1,0,0,2,5,7,2,9,6,6,2,6,8,1,9,7,8,8,9,5,1,1,4,2,0,1,3,6,7,8,7,0,5,6,0,1,7,9,6,4,8,6,7,0,2,3,2,7,6,0,5,0,9,0,3,3,8,5,0,9,3,8,0,1,3,1,8,1,8,1,1,7,5,7,4,1,0,0,0,8,9,5,7,8,9,2,8,3,0,3,4,9,8,1,7,2,3,8,3,5,3,1,4,7,7,5,4,9,2,6,2,6,4,0,0,2,8,3,3,0,9,1,6,8,3,1,7,0,7,1,5,8,3,2,5,1,1,0,3,1,4,6,3,6,2,8,6,7,2,9,5,9,1,6,0,5,4,8,6,6,9,4,0,5,8,7,0,8,9,7,3,9,0,1,0,6,2,7,3,3,2,3,3,6,3,0,8,0,0,5,2,1,0,7,5,0,3,2,6,0,5,4,9,6,7,1,0,4,0,9,6,8,3,1,2,5,0,1,0,6,8,6,6,8,8,2,4,5,0,0,8,0,5,6,2,2,5,6,3,7,7,8,4,8,4,8,9,1,6,8,9,9,0,4,0,5,5,4,9,6,7,7,9,0,5,0,9,2,5,2,9,8,9,7,6,8,6,9,2,9,1,6,0,2,7,4,4,5,3,4,5,5,5,0,8,1,3,8,3,0,8,5,7,6,8,7,8,9,7,0,8,4,0,7,0,9,5,8,2,0,8,7,0,3,1,8,1,7,1,6,9,7,9,7,2,6,3,0,5,3,6,0,5,9,3,9,1,1,0,0,8,1,4,3,0,4,3,7,7,7,4,6,4,0,0,5,7,3,2,8,5,1,4,5,8,5,6,7,5,7,3,3,9,6,8,1,5,1,1,1,0,3]
    k = 500
    print(maxNumber(nums1, nums2, k))