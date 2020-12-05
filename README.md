# Leetcode-Problem-Set

### [976-三角形的最大周长(S)](https://leetcode-cn.com/problems/largest-perimeter-triangle/)：[Code](https://github.com/LobbyBoy-Dray/Leetcode-Problem-Set/blob/master/code/0976-简单-三角形的最大周长.py)

> "难的又不会，只能做做简单题混混每日打卡这样子"‘

上来就想用递归，然后想用排序+DP——dp[i]表示以A[i]为最长边的可行三角形的最大周长。但紧接着就发现状态转移方程写不出来，或者说根本不需要状态转移……因为A[i-2]和A[i-1]如果不能和A[i]构成三角形的话，那更前面的A[i-k]就更不行了（可行三角形的充要条件：两条较短边之和大于最长的一边），所以排序后单指针遍历即可。

**Note**：一开始用从前往后遍历，发现只击败了10%+；看评论才意识到从后遍历这种贪心做法更快，还是太naive了……

### [767-重构字符串(M)](https://leetcode-cn.com/problems/reorganize-string/)：[Code](https://github.com/LobbyBoy-Dray/Leetcode-Problem-Set/blob/master/code/0767-中等-重构字符串.py)

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

**Note**：挖个坑，官方题解以及其他coder都说用“最大堆”很巧妙，明后天抽空学一下。

### [34-在排序数组中查找元素的第一个和最后一个位置(M)](https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/)：[Code](https://github.com/LobbyBoy-Dray/Leetcode-Problem-Set/blob/master/code/0034-中等-在排序数组中查找元素的第一个和最后一个位置.py)

>"今天终于可以重拳出击了。"

主要使用的方法还是二分查找：

* 首先，用二分法找到第一个target所在位置loc——如果连第一个都找不到的话，说明数组中就没有这个target，返回[-1,-1]即可；接着，对nums[:loc+1]和nums[loc:]两个数组分别再用二分，分别找最左侧和最右侧的target——一定能找到，因为再不济nums[loc]就是target；
* 怎么找最左侧的target？二分，如果nums[mid]等于target，暂存mid并令end=mid-1，即最左侧的target（如果存在）肯定还在左边子数组里；如果nums[mid]小于target，则令start=mid+1；不可能是nums[mid]大于target，因为原数组本来就是升序的。直到找完整个数组即可。最右侧的target找法类似。

### [321-拼接最大数(H)](https://leetcode-cn.com/problems/create-maximum-number/)：[Code](https://github.com/LobbyBoy-Dray/Leetcode-Problem-Set/blob/master/code/0321-困难-拼接最大数.py)

> "Computer Vision 计算机视觉，人工智能领域之一，简称CV，在该领域中的一切问题都可以通过：第一步：人工(按住键盘左下角那个键的同时，按住C)；第二步：智能，需要靠你大脑中亿万神经元的协同合作才能完成，你需要在屏幕中精确的选好位置，然后按下最下角那个键+V。这两步缺一不可！"

大的逻辑是：

* 将k分解为i+j，表示其中i个来自num1，j个来自num2——遍历所有available的(i,j)，获得最大的结果；
* 对于一个(i,j)：
  * ①从num1中拿到长度为i的最大数；从num2中拿到长度为j的最大数；
  * ②合并成一个数

其中，①步骤用DP做了大半天，但怎么调都超时（DP代码以注释形式保留）。看了题解，用单调栈通过。什么是单调栈：

* 在“还有名额”时，维持栈内的元素自底向顶是单调的；
* 本题中，在还可以删除元素时，向栈顶添加元素前，若栈顶的元素小，则弹出，直到：
  * 栈空了，弹不了了；OR
  * 删除的太多，已经没有删除名额了；OR
  * 栈顶的元素大于或等于要添加元素。
* 为什么栈顶元素小就要弹出：因为栈中一个元素，就对应着结果中的一位——栈顶小，那当然要用大的值来取代它了——一直弹，也就是把更大的数往高位去顶

### [204-计数质数(S)](https://leetcode-cn.com/problems/count-primes/)：[Code](https://github.com/LobbyBoy-Dray/Leetcode-Problem-Set/blob/master/code/0204-简单-计数质数.py)

> "写排名第一的那个答案的真他娘的是个人才，把特么20个测试用例全部写进去了。牛逼。"

正好之前在一本算法书的序言章节中看到过【埃氏筛法】的介绍，举个例子：

* 2 3 4 5 6 7 8 9 10 11 12 13 14 15
* 筛掉2的倍数(自己不筛): 2 3 5 7 9 11 13 15
* 筛掉3的倍数(自己不筛): 2 3 5 7 11 13——这里不用从2×3开始找，直接从3×3=9开始即可，因为2×3的那个数会被2的时候筛掉——筛p的倍数(自己不筛)，从p×p开始即可，p×(p+1)、p×(p+2)……
* 筛掉4的倍数(自己不筛)：2 3 5 7 11 13——不用，因为第一个要筛的为4*4=16，已经大于15了，算法停止。

### [659-分割数组为连续子序列(M)](https://leetcode-cn.com/problems/split-array-into-consecutive-subsequences/)：[Code](https://github.com/LobbyBoy-Dray/Leetcode-Problem-Set/blob/master/code/0659-中等-分割数组为连续子序列.py)

> "你们都在答题，只有我想斗地主"

核心：建立一个哈希表，key是数字，value是二叉堆（binaryheap）。

* 数字就是待一会儿要遍历数组，数组的每个数字就是那个key；
* 二叉堆表示的是，以key这个数字结尾的、所有连续子序列的长度，构建方法如下：
  * 如果存在以（key-1）这个数字结尾的连续子序列的话，取其中最短的那个长度加上1添加到该key的堆中，同时注意把（key-1）堆中相应的那个最短的长度删掉——这也是为啥选择用二叉堆这个数据结构（优先队列）——Note：这是一种贪心做法，用掉当前数字且尽量增长前面的短的子序列——那为啥不留下当前数字和后面的数字组序列？万一前面用太快后面的数字没得用了？——如果前面有可以续上的子序列而不续的话：情形一，后面的数字能和该数字续上，那还不如和当前数字一起续到前面短序列上；情形二，后面的数字和该数字续不上，那该数字就落单了。
  * 如果不存在以（key-1）这个数字结尾的连续子序列的话，那只能以改数字为开头做子序列，也就是给改数字的二叉堆添加一个1，表示加一个长度为1的子序列，等待看后面的数字能不能续上。
* 最后，遍历一遍哈希表，如果有哪个不为空的二叉堆的最小值小于3，那就说明拆解失败。

Note：二叉堆=完全二叉树+堆次序，本题用的最小堆，即root最小。

### [621-任务调度器](https://leetcode-cn.com/problems/task-scheduler/)：[Code](https://github.com/LobbyBoy-Dray/Leetcode-Problem-Set/blob/master/code/0621-中等-任务调度器.py)

>"可以将难度评价员开除了吗？？这是中等？？？明显是难为我胖某人"

