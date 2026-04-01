# LeetCode 42: 接雨水 (Trapping Rain Water)

## 1. 题目描述

给定 `n` 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

**示例 1:**
![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/22/rainwatertrap.png)

> 输入: height = [0,1,0,2,1,0,1,3,2,1,2,1]
> 输出: 6
> 解释: 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。

**示例 2:**

> 输入: height = [4,2,0,3,2,5]
> 输出: 9

**提示：**

* `n == height.length`
* `1 <= n <= 2 * 10^4`
* `0 <= height[i] <= 10^5`

---

## 2. 算法基本原理：双指针法 (基于您的思路演进)

这道题的核心在于**化整为零**，即“先思考第 `i` 个柱子上面能接多少水”。

**思路演进过程：**

1. **朴素解法 (按列求水)**：
   对于任意位置 `i`，它能接的水量取决于其**左侧最高柱子**和**右侧最高柱子**中的较小值。
   公式为：`water[i] = max(min(max(height[:i]), max(height[i+1:])) - height[i], 0)`。
   *缺点*：每次都要切片计算 `max(height[:i])` 和 `max(height[i+1:])`，时间复杂度高达 $O(N^2)$，会导致超时。

2. **双指针优化 (锁定短板)**：
   为了避免重复计算，我们使用左右双指针 `left = 0` 和 `right = len(height) - 1` 向中间逼近，并维护两个变量 `left_max` 和 `right_max`。
   
   * **核心逻辑**：根据木桶效应，决定当前柱子能接多少水的，是左右两侧最高柱子中的**较矮者**。
   * 如果 `height[left] < height[right]`：说明右侧一定存在一个比当前 `left` 更高（或相等）的柱子。此时，`left` 位置能接的水**完全由 `left_max` 决定**（因为右侧的真实最大值肯定大于等于 `height[right]`，也就大于 `height[left]`）。因此，我们可以放心地计算 `left` 处的水量，并将 `left` 指针右移。
   * 如果 `height[left] >= height[right]`：同理，右侧 `right` 位置能接的水完全由 `right_max` 决定，计算后将 `right` 指针左移。

**复杂度分析：**

* **时间复杂度**：$O(N)$，双指针只需遍历数组一次。
* **空间复杂度**：$O(1)$，仅使用了几个常数级别的变量。

---

## 3. 数学归纳法对算法的证明

**命题**：在双指针相遇前，每次移动指针所计算出的当前柱子接水量，都是全局最优且正确的。

**证明**：
假设当前左指针为 `left`，右指针为 `right`，且维护了 `left_max = max(height[0...left])` 和 `right_max = max(height[right...n-1])`。

* **情况 1：当 `height[left] < height[right]` 时**
  已知 `right_max >= height[right]`，所以 `right_max > height[left]`。
  对于 `left` 位置，其真实的右侧最大高度 `True_Right_Max` 必然满足 `True_Right_Max >= right_max > height[left]`。
  根据接水公式：`Water[left] = min(left_max, True_Right_Max) - height[left]`。
  因为 `left_max` 是从左向右更新的，此时 `left_max` 必然小于等于 `True_Right_Max`（因为 `True_Right_Max` 至少包含了 `height[right]`，而 `height[right] > height[left]`，且如果 `left_max` 很大，它早就大于 `height[right]` 从而走另一个分支了）。
  因此，`min(left_max, True_Right_Max)` 必然等于 `left_max`。
  结论：`Water[left] = left_max - height[left]` 成立。

* **情况 2：当 `height[left] >= height[right]` 时**
  同理可证，`right` 位置的真实左侧最大高度 `True_Left_Max >= height[left] >= height[right]`。
  因此 `min(True_Left_Max, right_max)` 必然等于 `right_max`。
  结论：`Water[right] = right_max - height[right]` 成立。



---

## 4. 编程中需要注意的小细节 (易错点)

1. **`left_max` 和 `right_max` 的更新时机**：
   先执行 `left_max = max(left_max, height[left])`，然后再计算 `total_water += left_max - height[left]`。这是一个非常安全的写法，因为如果当前柱子就是历史最高，`left_max - height[left]` 刚好等于 0，不会出现负数积水，天然处理了边界情况。
2. **最外侧柱子无法接水**：
   最开始的 left 和 right 是接不了水的。因为最外侧没有边界包裹。在代码逻辑中，最外侧柱子会直接更新 `left_max` 或 `right_max`，相减为 0。
3. **循环条件 `left < right`**：
   不需要写成 `left <= right`。当 `left == right` 时，两个指针指向同一个柱子，该柱子作为最后的最高点，其上方是不可能积水的（因为没有另一侧的边界了），所以循环到 `left < right` 结束即可。
