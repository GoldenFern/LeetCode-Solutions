from typing import List

class Solution:
    """
    LeetCode 300: 最长递增子序列
    使用 贪心 + 二分查找 算法求解，时间复杂度 O(n log n)
    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # tails[i] 存储长度为 i+1 的递增子序列的最小末尾元素
        tails = []
        
        for x in nums:
            # 使用二分查找在 tails 中寻找 x 的插入/替换位置
            idx = self._binary_search_left(tails, x)
            
            # 如果 idx 等于 tails 的长度，说明 x 比 tails 中所有元素都大
            if idx == len(tails):
                tails.append(x)  # 大的接后面，延长最长子序列
            else:
                tails[idx] = x   # 小的换中间，增加未来延长的潜力
                
        # tails 的长度就是最长递增子序列的长度
        return len(tails)

    def _binary_search_left(self, arr: List[int], target: int) -> int:
        """
        手写二分查找：寻找数组中第一个大于或等于 target 的元素的索引。
        (等价于 Python 内置的 bisect.bisect_left)
        """
        left = 0
        right = len(arr)
        
        # 注意这里的循环条件是 left < right
        while left < right:
            mid = left + (right - left) // 2  # 防止大数溢出的标准写法
            
            if arr[mid] < target:
                # target 严格大于中间值，说明目标在右半部分
                left = mid + 1
            else:
                # target 小于或等于中间值，说明目标在左半部分，或者就是 mid 本身
                # 所以 right 不能等于 mid - 1，必须保留 mid
                right = mid
                
        return left

if __name__ == "__main__":
    # 实例化解决方案类
    sol = Solution()
    
    # 定义测试用例：包含题目示例以及一些关键的边界情况
    # 格式: (输入数组, 期望的最长递增子序列长度)
    test_cases = [
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),  # 示例 1: 常规情况 (如 [2, 3, 7, 101])
        ([0, 1, 0, 3, 2, 3], 4),            # 示例 2: 包含 0 和重复数字
        ([7, 7, 7, 7, 7, 7], 1),            # 边界 1: 所有元素相同，严格递增长度为 1
        ([5, 4, 3, 2, 1], 1),               # 边界 2: 严格递减数组
        ([1, 2, 3, 4, 5], 5),               # 边界 3: 已经严格递增的数组
        ([4, 10, 4, 3, 8, 9], 3),           # 易错点: 测试替换逻辑是否正确执行
        ([], 0),                            # 边界 4: 空数组
        ([1], 1)                            # 边界 5: 只有一个元素
    ]
    
    # 批量执行测试
    for i, (nums, expected) in enumerate(test_cases):
        result = sol.lengthOfLIS(nums)
        print(f"Test Case {i+1}: Input = {nums}")
        print(f"  Expected = {expected}, Result = {result}")
        
        # 使用 assert 进行断言测试
        assert result == expected, f"Test Case {i+1} Failed!"
        
    print("\nAll test cases passed successfully! You have mastered Binary Search!")
