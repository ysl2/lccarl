# lccarl

## 数组

### [27. 移除元素](https://leetcode.cn/problems/remove-element/description)

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        for right in range(len(nums)):
            if nums[right] != val:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        return left
```

### [977. 有序数组的平方](https://leetcode.cn/problems/squares-of-a-sorted-array/description)

```python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        res = [0] * len(nums)
        p = len(nums) - 1
        while left <= right:
            x = nums[left] ** 2
            y = nums[right] ** 2
            if x > y:
                res[p] = x
                left += 1
                p -= 1
            else:
                res[p] = y
                right -= 1
                p -= 1
        return res
```

### [209. 长度最小的子数组](https://leetcode.cn/problems/minimum-size-subarray-sum/description)

```python
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window = 0
        res = inf
        left = 0
        for right in range(len(nums)):
            window += nums[right]
            while window >= target:
                res = min(res, right - left + 1)
                window -= nums[left]
                left += 1
        return res if res < inf else 0
```

### [59. 螺旋矩阵 II](https://leetcode.cn/problems/spiral-matrix-ii/description)

```python
DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        m = n
        size = n * n
        res = [[0] * n for _ in range(n)]
        i, j, di = 0, -1, 0
        num = 1
        while num <= size:
            dx, dy = DIRS[di]
            for _ in range(n):
                i += dx
                j += dy
                res[i][j] = num
                num += 1
            di = (di + 1) % len(DIRS)
            m, n = n, m - 1
        return res
```

### [303. 区域和检索 - 数组不可变 | 58. 区间和（第九期模拟笔试）](https://leetcode.cn/problems/range-sum-query-immutable/description)

```python
class NumArray:

    def __init__(self, nums: List[int]):
        self.cnt = [0]
        for num in nums:
            self.cnt.append(self.cnt[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        return self.cnt[right + 1] - self.cnt[left]
```

### 44. 开发商购买土地（第五期模拟笔试）（暂未找到力扣）

## 链表

### [203. 移除链表元素](https://leetcode.cn/problems/remove-linked-list-elements/description)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        p = dummy = ListNode(next=head)
        while p and p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return dummy.next
```

### [707. 设计链表](https://leetcode.cn/problems/design-linked-list/description)

## 哈希表

### [242. 有效的字母异位词](https://leetcode.cn/problems/valid-anagram/description)

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt = defaultdict(int)
        for c in s:
            cnt[c] += 1
        for c in t:
            cnt[c] -= 1
        return not any(cnt.values())
```

### [349. 两个数组的交集](https://leetcode.cn/problems/intersection-of-two-arrays/description)

```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
```

### [202. 快乐数](https://leetcode.cn/problems/happy-number/description)

```python
class Solution:
    def isHappy(self, n: int) -> bool:
        window = set()
        while n != 1 and n not in window:
            mp.add(n)
            n = sum(int(c) ** 2 for c in str(n))
        return n == 1
```

### [454. 四数相加 II](https://leetcode.cn/problems/4sum-ii/description)

```python
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        cnt = Counter(num1 + num2 for num1 in nums1 for num2 in nums2)
        return sum(cnt[-(num3 + num4)] for num3 in nums3 for num4 in nums4)
```

### [383. 赎金信](https://leetcode.cn/problems/ransom-note/description)

```python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return not (Counter(ransomNote) - Counter(magazine))
```

### [18. 四数之和](https://leetcode.cn/problems/4sum/description)

```python
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for first in range(n - 3):
            if first > 0 and nums[first - 1] == nums[first]:
                continue
            for second in range(first + 1, n - 2):
                if second > first + 1 and nums[second - 1] == nums[second]:
                    continue
                forth = n - 1
                sub_target = target - nums[first] - nums[second]
                for third in range(second + 1, n - 1):
                    if third > second + 1 and nums[third - 1] == nums[third]:
                        continue
                    while third < forth and nums[third] + nums[forth] > sub_target:
                        forth -= 1
                    if third == forth:
                        break
                    elif nums[third] + nums[forth] == sub_target:
                        res.append([nums[first], nums[second], nums[third], nums[forth]])
        return res
```

## 字符串

### [344. 反转字符串](https://leetcode.cn/problems/reverse-string/description)

```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
```

### [541. 反转字符串 II](https://leetcode.cn/problems/reverse-string-ii/description)

```python
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        for i in range(0, len(s), 2 * k):
            s[i : i + k] = reversed(s[i : i + k])
        return ''.join(s)
```

### 54. 替换数字（第八期模拟笔试）

### [151. 反转字符串中的单词](https://leetcode.cn/problems/reverse-words-in-a-string/description)

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])
```

### 55. 右旋字符串（第八期模拟笔试）

### [28. 找出字符串中第一个匹配项的下标](https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/description)

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        m, n = len(haystack), len(needle)
        mp = [0] * n
        left = 0
        for right in range(1, n):
            while left > 0 and needle[left] != needle[right]:
                left = mp[left - 1]
            if needle[left] == needle[right]:
                left += 1
            mp[right] = left
        left = 0
        for right in range(m):
            while left > 0 and needle[left] != haystack[right]:
                left = mp[left - 1]
            if needle[left] == haystack[right]:
                left += 1
            if left == n:
                return right - n + 1
        return -1
```

### [459. 重复的子字符串](https://leetcode.cn/problems/repeated-substring-pattern/description)

```python
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        if n == 0:
            return False
        mp = [0] * n
        left = 0
        for right in range(1, n):
            while left > 0 and s[left] != s[right]:
                left = mp[left - 1]
            if s[left] == s[right]:
                left += 1
            mp[right] = left
        return mp[-1] > 0 and n % (n - mp[-1]) == 0
```

## 栈与队列

### [232. 用栈实现队列](https://leetcode.cn/problems/implement-queue-using-stacks/description)

```python
class MyQueue:

    def __init__(self):
        self.a, self.b = [], []

    def push(self, x: int) -> None:
        self.a.append(x)

    def move(self):
        if not self.b:
            while self.a:
                self.b.append(self.a.pop())

    def pop(self) -> int:
        self.move()
        return self.b.pop()

    def peek(self) -> int:
        self.move()
        return self.b[-1]

    def empty(self) -> bool:
        return not self.a and not self.b
```

### [225. 用队列实现栈](https://leetcode.cn/problems/implement-stack-using-queues/description)

```python
class MyStack:

    def __init__(self):
        self.a, self.b = deque(), deque()

    def push(self, x: int) -> None:
        self.a.append(x)

    def pot(self, fn=''):
        while len(self.a) > 1:
            self.b.append(self.a.popleft())
        res = self.a.popleft()
        if fn == 'top':
            self.b.append(res)
        self.a, self.b = self.b, self.a
        return res

    def pop(self) -> int:
        return self.pot(fn='pop')

    def top(self) -> int:
        return self.pot(fn='top')

    def empty(self) -> bool:
        return not self.a and not self.b
```

### [1047. 删除字符串中的所有相邻重复项](https://leetcode.cn/problems/remove-all-adjacent-duplicates-in-string/description)
### [150. 逆波兰表达式求值](https://leetcode.cn/problems/evaluate-reverse-polish-notation/description)

## 二叉树

### [111. 二叉树的最小深度](https://leetcode.cn/problems/minimum-depth-of-binary-tree/description)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([(root, 1)])
        while q:
            node, depth = q.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                q.append((node.left, depth + 1))
            if node.right:
                q.append((node.right, depth + 1))
        return 0
```

### [222. 完全二叉树的节点个数](https://leetcode.cn/problems/count-complete-tree-nodes/description)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left, right = root.left, root.right
        left_depth, right_depth = 0, 0
        while left:
            left = left.left
            left_depth += 1
        while right:
            right = right.right
            right_depth += 1
        if left_depth == right_depth:
            return (2 << left_depth) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
```

### [110. 平衡二叉树](https://leetcode.cn/problems/balanced-binary-tree/description)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return 0
            if (l := dfs(root.left)) == -1:
                return -1
            if (r := dfs(root.right)) == -1:
                return -1
            if abs(l - r) > 1:
                return -1
            return max(l, r) + 1
        return dfs(root) != -1
```

### [257. 二叉树的所有路径](https://leetcode.cn/problems/binary-tree-paths/description)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def dfs(root, tmp):
            if not root:
                return
            tmp = tmp + [str(root.val)]
            if not root.left and not root.right:
                res.append('->'.join(tmp))
                return
            dfs(root.left, tmp)
            dfs(root.right, tmp)
        dfs(root, [])
        return res
```

### [404. 左叶子之和](https://leetcode.cn/problems/sum-of-left-leaves/description)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(root):
            if not root:
                return
            if root.left and not root.left.left and not root.left.right:
                self.res += root.left.val
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return self.res
```

### [513. 找树左下角的值](https://leetcode.cn/problems/find-bottom-left-tree-value/description)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        while q:
            node = q.popleft()
            # Right first, then left.
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
        return node.val
```

### [112. 路径总和](https://leetcode.cn/problems/path-sum/description)
### [106. 从中序与后序遍历序列构造二叉树](https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description)
### [654. 最大二叉树](https://leetcode.cn/problems/maximum-binary-tree/description)
### [617. 合并二叉树](https://leetcode.cn/problems/merge-two-binary-trees/description)
### [700. 二叉搜索树中的搜索](https://leetcode.cn/problems/search-in-a-binary-search-tree/description)
### [530. 二叉搜索树的最小绝对差](https://leetcode.cn/problems/minimum-absolute-difference-in-bst/description)
### [501. 二叉搜索树中的众数](https://leetcode.cn/problems/find-mode-in-binary-search-tree/description)
### [235. 二叉搜索树的最近公共祖先](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-search-tree/description)
### [701. 二叉搜索树中的插入操作](https://leetcode.cn/problems/insert-into-a-binary-search-tree/description)
### [450. 删除二叉搜索树中的节点](https://leetcode.cn/problems/delete-node-in-a-bst/description)
### [669. 修剪二叉搜索树](https://leetcode.cn/problems/trim-a-binary-search-tree/description)
### [538. 把二叉搜索树转换为累加树](https://leetcode.cn/problems/convert-bst-to-greater-tree/description)

## 回溯算法

### [77. 组合](https://leetcode.cn/problems/combinations/description)

```python
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(i, tmp):
            if len(tmp) == k:
                res.append(tmp)
                return
            for j in range(i, n + 1):
                dfs(j + 1, tmp + [j])
        dfs(1, [])
        return res
```

### [216. 组合总和 III](https://leetcode.cn/problems/combination-sum-iii/description)

```python
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def dfs(i, tmp):
            if sum(tmp) == n and len(tmp) == k:
                res.append(tmp)
                return
            for j in range(1, i):
                dfs(j, tmp + [j])
        dfs(10, [])
        return res
```

### [40. 组合总和 II](https://leetcode.cn/problems/combination-sum-ii/description)

```python
class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        def dfs(nums, tmp):
            if sum(tmp) == target:
                res.append(tmp)
                return
            for i in range(len(nums)):
                if nums[i] > target - sum(tmp):
                    break
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                dfs(nums[i + 1:], tmp + [nums[i]])
        dfs(nums, [])
        return res
```

### [93. 复原 IP 地址](https://leetcode.cn/problems/restore-ip-addresses/description)

```python
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def dfs(s, tmp):
            if not s and len(tmp) == 4:
                res.append('.'.join(tmp))
                return
            if not s or len(tmp) == 4:
                return
            for i in range(1, min(4, len(s) + 1)):
                t = s[:i]
                if (i > 1 and s[0] == '0') or int(t) > 255:
                    continue
                dfs(s[i:], tmp + [t])
        dfs(s, [])
        return res
```

### [90. 子集 II](https://leetcode.cn/problems/subsets-ii/description)

```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def dfs(nums, tmp):
            res.append(tmp)
            if not nums:
                return
            for i in range(len(nums)):
                if i > 0 and nums[i - 1] == nums[i]:
                    continue
                dfs(nums[i + 1:], tmp + [nums[i]])
        dfs(nums, [])
        return res
```

### [491. 非递减子序列](https://leetcode.cn/problems/non-decreasing-subsequences/description)
### [47. 全排列 II](https://leetcode.cn/problems/permutations-ii/description)
### [332. 重新安排行程](https://leetcode.cn/problems/reconstruct-itinerary/description)
### [37. 解数独](https://leetcode.cn/problems/sudoku-solver/description)
## 贪心算法
### [455. 分发饼干](https://leetcode.cn/problems/assign-cookies/description)
### [376. 摆动序列](https://leetcode.cn/problems/wiggle-subsequence/description)
### [122. 买卖股票的最佳时机 II](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/description)
### [1005. K 次取反后最大化的数组和](https://leetcode.cn/problems/maximize-sum-of-array-after-k-negations/description)
### [134. 加油站](https://leetcode.cn/problems/gas-station/description)
### [135. 分发糖果](https://leetcode.cn/problems/candy/description)
### [860. 柠檬水找零](https://leetcode.cn/problems/lemonade-change/description)
### [406. 根据身高重建队列](https://leetcode.cn/problems/queue-reconstruction-by-height/description)
### [452. 用最少数量的箭引爆气球](https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/description)
### [435. 无重叠区间](https://leetcode.cn/problems/non-overlapping-intervals/description)
### [738. 单调递增的数字](https://leetcode.cn/problems/monotone-increasing-digits/description)
### [968. 监控二叉树](https://leetcode.cn/problems/binary-tree-cameras/description)
## 动态规划
### [509. 斐波那契数](https://leetcode.cn/problems/fibonacci-number/description)
### [746. 使用最小花费爬楼梯](https://leetcode.cn/problems/min-cost-climbing-stairs/description)
### [63. 不同路径 II](https://leetcode.cn/problems/unique-paths-ii/description)
### [343. 整数拆分](https://leetcode.cn/problems/integer-break/description)
### [96. 不同的二叉搜索树](https://leetcode.cn/problems/unique-binary-search-trees/description)
### 46. 携带研究材料（第六期模拟笔试）
### [1049. 最后一块石头的重量 II](https://leetcode.cn/problems/last-stone-weight-ii/description)
### [494. 目标和](https://leetcode.cn/problems/target-sum/description)
### [474. 一和零](https://leetcode.cn/problems/ones-and-zeroes/description)
### 52. 携带研究材料（第七期模拟笔试）
### [518. 零钱兑换 II](https://leetcode.cn/problems/coin-change-ii/description)
### [377. 组合总和 Ⅳ](https://leetcode.cn/problems/combination-sum-iv/description)
### 57. 爬楼梯（第八期模拟笔试）
### 56. 携带矿石资源（第八期模拟笔试）
### [213. 打家劫舍 II](https://leetcode.cn/problems/house-robber-ii/description)
### [337. 打家劫舍 III](https://leetcode.cn/problems/house-robber-iii/description)
### [122. 买卖股票的最佳时机 II](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/description)
### [123. 买卖股票的最佳时机 III](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iii/description)
### [188. 买卖股票的最佳时机 IV](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/description)
### [309. 买卖股票的最佳时机含冷冻期](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-cooldown/description)
### [714. 买卖股票的最佳时机含手续费](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description)
### [674. 最长连续递增序列](https://leetcode.cn/problems/longest-continuous-increasing-subsequence/description)
### [718. 最长重复子数组](https://leetcode.cn/problems/maximum-length-of-repeated-subarray/description)
### [1035. 不相交的线](https://leetcode.cn/problems/uncrossed-lines/description)
### [392. 判断子序列](https://leetcode.cn/problems/is-subsequence/description)
### [115. 不同的子序列](https://leetcode.cn/problems/distinct-subsequences/description)
### [583. 两个字符串的删除操作](https://leetcode.cn/problems/delete-operation-for-two-strings/description)
### [647. 回文子串](https://leetcode.cn/problems/palindromic-substrings/description)
### [516. 最长回文子序列](https://leetcode.cn/problems/longest-palindromic-subsequence/description)
## 单调栈
### [496. 下一个更大元素 I](https://leetcode.cn/problems/next-greater-element-i/description)
### [503. 下一个更大元素 II](https://leetcode.cn/problems/next-greater-element-ii/description)
## 图论
### [797. 所有可能的路径 | 98. 所有可达路径（卡码网）](https://leetcode.cn/problems/all-paths-from-source-to-target/description)
### [695. 岛屿的最大面积 | 100. 岛屿的最大面积（卡码网）](https://leetcode.cn/problems/max-area-of-island/description)
### 101. 孤岛的总面积（卡码网）（暂未找到力扣）
### 102. 沉没孤岛（卡码网）（暂未找到力扣）
### [417. 太平洋大西洋水流问题 | 103. 水流问题（卡码网）](https://leetcode.cn/problems/pacific-atlantic-water-flow/description)
### [827. 最大人工岛 | 104. 建造最大岛屿（卡码网）](https://leetcode.cn/problems/making-a-large-island/description)
### [127. 单词接龙 | 110. 字符串接龙（卡码网）](https://leetcode.cn/problems/word-ladder/description)
### 105. 有向图的完全可达性（卡码网）
### [463. 岛屿的周长 | 106. 岛屿的周长（卡码网）](https://leetcode.cn/problems/island-perimeter/description)
### 107. 寻找存在的路径（卡码网）
### 108. 冗余连接（卡码网）
### 109. 冗余连接II（卡码网）
### 53. 寻宝（第七期模拟笔试）
### 117. 软件构建（卡码网）
### 47. 参加科学大会（第六期模拟笔试）
### 94. 城市间货物运输 I（卡码网）
### 95. 城市间货物运输 II（卡码网）
### 96. 城市间货物运输 III（卡码网）
### 97. 小明逛公园（卡码网）
### 127. 骑士的攻击（卡码网）
## 额外题目
### [1365. 有多少小于当前数字的数字](https://leetcode.cn/problems/how-many-numbers-are-smaller-than-the-current-number/description)
### [941. 有效的山脉数组](https://leetcode.cn/problems/valid-mountain-array/description)
### [1207. 独一无二的出现次数](https://leetcode.cn/problems/unique-number-of-occurrences/description)
### [724. 寻找数组的中心下标](https://leetcode.cn/problems/find-pivot-index/description)
### [922. 按奇偶排序数组 II](https://leetcode.cn/problems/sort-array-by-parity-ii/description)
### [143. 重排链表](https://leetcode.cn/problems/reorder-list/description)
### [205. 同构字符串](https://leetcode.cn/problems/isomorphic-strings/description)
### [1002. 查找共用字符](https://leetcode.cn/problems/find-common-characters/description)
### [925. 长按键入](https://leetcode.cn/problems/long-pressed-name/description)
### [844. 比较含退格的字符串](https://leetcode.cn/problems/backspace-string-compare/description)
### [129. 求根节点到叶节点数字之和](https://leetcode.cn/problems/sum-root-to-leaf-numbers/description)
### [1382. 将二叉搜索树变平衡](https://leetcode.cn/problems/balance-a-binary-search-tree/description)
### [100. 相同的树](https://leetcode.cn/problems/same-tree/description)
### [116. 填充每个节点的下一个右侧节点指针](https://leetcode.cn/problems/populating-next-right-pointers-in-each-node/description)
### [52. N 皇后 II](https://leetcode.cn/problems/n-queens-ii/description)
### [649. Dota2 参议院](https://leetcode.cn/problems/dota2-senate/description)
### [1221. 分割平衡字符串](https://leetcode.cn/problems/split-a-string-in-balanced-strings/description)
### [132. 分割回文串 II](https://leetcode.cn/problems/palindrome-partitioning-ii/description)
### [673. 最长递增子序列的个数](https://leetcode.cn/problems/number-of-longest-increasing-subsequence/description)
### [841. 钥匙和房间](https://leetcode.cn/problems/keys-and-rooms/description)
### [127. 单词接龙](https://leetcode.cn/problems/word-ladder/description)
### [684. 冗余连接](https://leetcode.cn/problems/redundant-connection/description)
### [685. 冗余连接 II](https://leetcode.cn/problems/redundant-connection-ii/description)
### [657. 机器人能否返回原点](https://leetcode.cn/problems/robot-return-to-origin/description)
### [463. 岛屿的周长](https://leetcode.cn/problems/island-perimeter/description)
### [1356. 根据数字二进制下 1 的数目排序](https://leetcode.cn/problems/sort-integers-by-the-number-of-1-bits/description)
