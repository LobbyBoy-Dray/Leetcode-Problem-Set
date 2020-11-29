# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/
# 给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。
# 请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
# 你可以假设 nums1 和 nums2 不会【同时】为空。

nums1 = [1, 2]
nums2 = []

def findMedian(nums1, nums2):
    ######################################################
    (short,long)  = (nums1,nums2) if len(nums1)<=len(nums2) else (nums2,nums1)
    short_length  = len(short)
    long_length   = len(long)
    #################如果一个列表为空######################
    if short_length == 0:
        if long_length % 2 == 0:
            return (long[long_length//2] + long[long_length//2-1]) / 2
        else:
            return long[long_length//2]
    ###################否则进入二分查找####################
    low           = 0
    high          = short_length
    sl            = (low + high)//2
    found         = False
    while not found:
        ll = (short_length + long_length - 1)//2 - sl + 1
        ######################################################
        if short[:sl] == []:
            leftMax   = long[ll-1]
            changeLow = True
        elif long[:ll] == []:
            leftMax = short[sl-1]
            changeLow = False
        else:
            if short[sl-1] > long[ll-1]:
                leftMax = short[sl-1]
                changeLow = False
            else:
                leftMax = long[ll-1]
                changeLow = True
        ######################################################
        if short[sl:] == []:
            rightMin  = long[ll]
        elif long[ll:] == []:
            rightMin = short[sl]
        else:
            if short[sl] < long[ll]:
                rightMin = short[sl]
            else:
                rightMin = long[ll]
        ######################################################
        if leftMax <= rightMin:
            found = True
        else:
            if changeLow:
                low = sl + 1
            else:
                high = sl - 1
            sl = (low + high)//2
    if (short_length + long_length)%2 == 0:
        return (leftMax + rightMin) / 2
    else:
        return leftMax

print(findMedian(nums1,nums2))

            





