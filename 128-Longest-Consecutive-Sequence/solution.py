from typing import List

class Solution:
    """
    LeetCode 128: 最长连续序列
    包含四种解法：哈希表、动态规划、排序+滑动窗口、暴力枚举
    """

    def longestConsecutive_hash(self, nums: List[int]) -> int:
        """
        解法一：哈希表 (最优解)
        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        # 1. 将列表转换为哈希集合，去重的同时保证后续的 in 操作是 O(1) 的时间复杂度
        # 注意：这一步绝对不能省，否则后续的 in 操作会退化为 O(n)
        num_set = set(nums)
        longest_streak = 0

        for num in num_set:
            # 2. 核心剪枝：仅当 num 是某个连续序列的起点时，才开始计算
            # 强调：必须排除不是起点的元素，否则时间复杂度会退化为 O(n^2)
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                # 3. 从起点开始，不断在哈希表中查找下一个连续的数字
                # 强调：这里的 in 操作因为是针对 set，所以符合哈希的 O(1) 查找
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak

    def longestConsecutive_dp(self, nums: List[int]) -> int:
        """
        解法二：动态规划 (基于排序)
        时间复杂度：O(n log n)
        空间复杂度：O(n)
        """
        if not nums:
            return 0
            
        nums.sort()
        n = len(nums)
        # dp[i] 记录以 nums[i] 结尾的连续序列长度
        dp = [1] * n
        longest_streak = 1
        
        for i in range(1, n):
            if nums[i] == nums[i-1] + 1:
                dp[i] = dp[i-1] + 1
            elif nums[i] == nums[i-1]:
                # 遇到重复元素，保持当前长度不变（或者设为 dp[i-1]）
                dp[i] = dp[i-1]
            else:
                dp[i] = 1
            longest_streak = max(longest_streak, dp[i])
            
        return longest_streak

    def longestConsecutive_sort(self, nums: List[int]) -> int:
        """
        解法三：排序 + 滑动窗口/双指针
        时间复杂度：O(n log n) - 瓶颈在于排序
        空间复杂度：O(1) 或 O(n) - 取决于排序算法
        """
        if not nums:
            return 0

        nums.sort()
        longest_streak = 1
        current_streak = 1

        for i in range(1, len(nums)):
            # 遇到重复元素，直接跳过
            if nums[i] == nums[i - 1]:
                continue
            # 遇到连续元素，当前长度 +1
            if nums[i] == nums[i - 1] + 1:
                current_streak += 1
            # 元素不连续，结算当前长度，并重置为 1
            else:
                longest_streak = max(longest_streak, current_streak)
                current_streak = 1

        # 循环结束后还需要再比较一次，防止最长序列在数组末尾
        return max(longest_streak, current_streak)

    def longestConsecutive_brute(self, nums: List[int]) -> int:
        """
        解法四：暴力枚举
        时间复杂度：O(n^3) - 外层 O(n)，内层 while 循环 O(n)，in list 查找 O(n)
        空间复杂度：O(1)
        注意：此方法在 LeetCode 提交会 Time Limit Exceeded (超时)
        """
        longest_streak = 0

        for num in nums:
            current_num = num
            current_streak = 1

            # 致命缺陷：在 list 中使用 in 操作，每次查找都是 O(n)
            while current_num + 1 in nums:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

        return longest_streak


if __name__ == "__main__":
    sol = Solution()
    
    # 测试用例：(输入数组, 期望输出)
    test_cases = [
        ([100, 4, 200, 1, 3, 2], 4),          # 示例 1：常规情况
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),  # 示例 2：包含重复元素和 0
        ([1, 0, 1, 2], 3),                    # 示例 3：重复元素不影响连续长度
        ([], 0),                              # 边界情况：空数组
        ([5], 1),                             # 边界情况：只有一个元素
        ([1, 2, 0, 1], 3),                    # 边界情况：跨越 0 的连续序列
        ([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6], 7) # 包含负数的情况
    ]
    
    # 将四种方法放入列表中批量测试
    methods = [
        ("解法一：哈希表 (O(n))", sol.longestConsecutive_hash),
        ("解法二：动态规划 (O(n log n))", sol.longestConsecutive_dp),
        ("解法三：排序法 (O(n log n))", sol.longestConsecutive_sort),
        ("解法四：暴力枚举 (O(n^3))", sol.longestConsecutive_brute)
    ]

    for method_name, method_func in methods:
        print(f"========== 测试 {method_name} ==========")
        for i, (nums, expected) in enumerate(test_cases):
            # 注意：传入 nums.copy() 防止排序解法修改原数组，影响后续测试
            result = method_func(nums.copy())
            
            # 断言测试
            assert result == expected, f"Test Case {i+1} Failed! Expected {expected}, Got {result}"
            print(f"  [Pass] Test Case {i+1}: Input length {len(nums)} -> Result: {result}")
        print("\n")
        
    print("🎉 所有解法的测试用例均已通过！")
