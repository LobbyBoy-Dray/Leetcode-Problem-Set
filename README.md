# Leetcode-Problem-Set

### [976-三角形的最大周长(S)](https://leetcode-cn.com/problems/largest-perimeter-triangle/)：[Code](https://github.com/LobbyBoy-Dray/Leetcode-Problem-Set/blob/master/code/976-%E7%AE%80%E5%8D%95-%E4%B8%89%E8%A7%92%E5%BD%A2%E7%9A%84%E6%9C%80%E5%A4%A7%E5%91%A8%E9%95%BF.py)

> "难的又不会，只能做做简单题混混每日打卡这样子"‘

上来就想用递归，然后想用排序+DP——dp[i]表示以A[i]为最长边的可行三角形的最大周长。但紧接着就发现状态转移方程写不出来，或者说根本不需要状态转移……因为A[i-2]和A[i-1]如果不能和A[i]构成三角形的话，那更前面的A[i-k]就更不行了（可行三角形的充要条件：两条较短边之和大于最长的一边），所以排序后单指针遍历即可。

Note：一开始用从前往后遍历，发现只击败了10%+；看评论才意识到从后遍历这种贪心做法更快，还是太naive了……

### [767-重构字符串(M)](https://leetcode-cn.com/problems/reorganize-string/)：[Code](https://github.com/LobbyBoy-Dray/Leetcode-Problem-Set/blob/master/code/767-%E4%B8%AD%E7%AD%89%E9%87%8D%E6%9E%84%E5%AD%97%E7%AC%A6%E4%B8%B2.py)

> "为什么方法一图里有一个醒目的 sb？仿佛在人身攻击我(;´༎ຶД༎ຶ`)"

把出现次数最多的字母X挑出来，用剩下的字母来插空。

* 插空之前，如果字符串总长度小于【2×X出现次数-1】，那么肯定不能构建出满足题意的目标字符串——例如aaaabb，两个其他字符不够插三个空的，所以必有两个a连在一起；
* 如果过了上面的条件判断，那么一定可以构建出目标字符串的，构建方法：用【其他字符】开始插空，插完一轮后继续插，直到用完所有其他字符——例如：aaaabbccc
  * aaaa
  * abaaa（插一个b）
  * ababaa（再插一个b，b用完）
  * ababaca（插一个c）
  * ababacac（再插一个c，此时一轮插完，从头再插）
  * acbabacac（所有其他字符插完，结束）
* Why上面的插法不会有相邻字符是一样的？如果有相邻字符是一样的，那意味着，有一个字符出现了很多次，以至于它插完了所有的空又轮了回来——但我们知道空的数量等于出现最多的字符出现的次数，所以不会再有字符出现比这个更多次了，所以不会出现上述情况。

Note：挖个坑，官方题解以及其他coder都说用“最大堆”很巧妙，明后天抽空学一下。