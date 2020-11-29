# Leetcode-Problem-Set

## 2019-11-29

#### [三角形的最大周长-976-简单](https://leetcode-cn.com/problems/largest-perimeter-triangle/)——[Code](https://github.com/LobbyBoy-Dray/Leetcode-Problem-Set/blob/master/code/976-%E7%AE%80%E5%8D%95-%E4%B8%89%E8%A7%92%E5%BD%A2%E7%9A%84%E6%9C%80%E5%A4%A7%E5%91%A8%E9%95%BF.py)

> "难的又不会，只能做做简单题混混每日打卡这样子"‘

上来就想用递归，然后想用排序+DP——dp[i]表示以A[i]为最长边的可行三角形的最大周长。但紧接着就发现状态转移方程写不出来，或者说根本不需要状态转移……因为A[i-2]和A[i-1]如果不能和A[i]构成三角形的话，那更前面的A[i-k]就更不行了（可行三角形的充要条件：两条较短边之和大于最长的一边），所以排序后单指针遍历即可。

Note：一开始用从前往后遍历，发现只击败了10%+；看评论才意识到从后遍历这种贪心做法更快，还是太naive了……
