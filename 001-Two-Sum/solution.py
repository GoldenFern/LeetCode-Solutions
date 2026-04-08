from typing import List

class Solution:
    """
    LeetCode 1: 两数之和
    利用哈希表 (dict) 的 O(1) 平均查找时间实现线性复杂度。
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 建立哈希表：{数值: 索引}
        # Python 的 dict 在底层使用开放寻址法处理冲突
        prev_nums = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            # 步骤 1: 在哈希表中查找补数 (平均 O(1))
            if complement in prev_nums:
                # 如果找到，说明 complement 是之前出现过的，直接返回结果
                return [prev_nums[complement], i]
            
            # 步骤 2: 如果没找到，将当前数存入哈希表，供后续数字匹配
            # 注意：必须先查找再存入，防止同一个元素被重复计算
            prev_nums[num] = i
            
        return []

if __name__ == "__main__":
    sol = Solution()
    
    # 测试用例集
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),   # 常规情况
        ([3, 2, 4], 6, [1, 2]),        # 补数在后面
        ([3, 3], 6, [0, 1]),           # 相同数字的情况
        ([-1, -2, -3], -5, [1, 2]),    # 负数情况
    ]
    
    print("Running tests...")
    for nums, target, expected in test_cases:
        result = sol.twoSum(nums, target)
        # 结果可能顺序不同，排序后断言
        assert sorted(result) == sorted(expected), f"Failed on {nums}, target {target}"
        print(f"Success: nums={nums}, target={target} -> result={result}")
        
    print("\nAll test cases passed!")
