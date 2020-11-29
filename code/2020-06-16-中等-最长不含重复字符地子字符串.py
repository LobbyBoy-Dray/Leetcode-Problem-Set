# 【最长不含重复字符的子字符串】
# 请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。
# 输入: "pwwkew"
# 输出: 3

def lengthOfLongestSubstring(s):
    if s == "":
        return 0
    sLength  = len(s)
    # 对于每个位置都维持两个数据：
    # 第一，到目前位置为止最长的目标字符串的长度；
    # 第二，一个子字符串的长度，该子字符串从某一位到字符串末尾，且不含重复字符，最长
    dpResult = dict()
    # 遍历字符串的每一位
    for index in range(sLength):
        thisChar = s[index]
        if index == 0:
            maxLength      = 1
            rearFirstIndex = 0
        else:
            lastMaxLength      = dpResult[index-1][0]
            lastRearFirstIndex = dpResult[index-1][1]
            rearSubStr         = s[lastRearFirstIndex:index]
            if thisChar in rearSubStr:
                rearFirstIndex = lastRearFirstIndex + rearSubStr.index(thisChar) + 1
            else:
                rearFirstIndex = lastRearFirstIndex
            maxLength          = lastMaxLength if lastMaxLength >= (index-rearFirstIndex+1) else (index-rearFirstIndex+1)
        dpResult[index] = [maxLength, rearFirstIndex]
    return dpResult[sLength-1][0]

print(lengthOfLongestSubstring("pwwkew"))