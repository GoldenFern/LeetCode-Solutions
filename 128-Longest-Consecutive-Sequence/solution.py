from typing import List

class Solution:
    """
    LeetCode 128: 最长连续序列
    使用 哈希表 (Hash Set) 求解，满足 O(n) 时间复杂度。
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        # 1. 将列表转换为哈希集合，去重的同时保证后续的 in 操作是 O(1) 的时间复杂度
        num_set = set(nums)
        longest_streak = 0

        # 2. 遍历哈希集合中的每一个数字
        for num in num_set:
            # 3. 核心剪枝：仅当 num 是某个连续序列的起点时，才开始计算
            # 也就是说，如果 num - 1 存在于集合中，说明 num 只是某个序列的中间节点，直接跳过
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                # 4. 从起点开始，不断在哈希表中查找下一个连续的数字
                # 这里的 in 操作因为是针对 set，所以是 O(1) 的
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                # 5. 更新全局最长序列长度
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
        ([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6], 7) # 包含负数的情况 (-1, 0, 1) 和 (3,4,5,6,7,8,9)
    ]
    
    for i, (nums, expected) in enumerate(test_cases):
        result = sol.longestConsecutive(nums)
        print(f"Test Case {i+1}:")
        print(f"  Input: {nums}")
        print(f"  Expected: {expected}, Got: {result}")
        assert result == expected, f"Test Case {i+1} Failed!"
        print("  -> Passed\n")
        
    print("All test cases passed successfully!")
