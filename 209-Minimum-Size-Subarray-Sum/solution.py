from typing import List

class Solution:
    """
    LeetCode 209: 长度最小的子数组
    """
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        使用滑动窗口（同向双指针）寻找满足和 >= target 的最短连续子数组。
        
        :param target: 目标和
        :param nums: 正整数数组
        :return: 最短子数组的长度，若不存在则返回 0
        """
        n = len(nums)
        left = 0
        current_sum = 0
        min_len = float('inf')
        
        # right 指针主动向右扩张窗口
        for right in range(n):
            current_sum += nums[right]
            
            # 当窗口内的和满足条件时，尝试缩小窗口（left 指针向右收缩）
            while current_sum >= target:
                # 记录当前满足条件的最小长度
                min_len = min(min_len, right - left + 1)
                # 移出左边界元素，窗口缩小
                current_sum -= nums[left]
                left += 1
                
        return 0 if min_len == float('inf') else min_len

if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例 1：题目示例
    target1, nums1 = 7, [2, 3, 1, 2, 4, 3]
    print(f"Test 1: target={target1}, nums={nums1}")
    print(f"Output: {solution.minSubArrayLen(target1, nums1)} (Expected: 2)\n")
    
    # 测试用例 2：题目示例
    target2, nums2 = 4, [1, 4, 4]
    print(f"Test 2: target={target2}, nums={nums2}")
    print(f"Output: {solution.minSubArrayLen(target2, nums2)} (Expected: 1)\n")
    
    # 测试用例 3：无解的情况
    target3, nums3 = 11, [1, 1, 1, 1, 1, 1, 1, 1]
    print(f"Test 3: target={target3}, nums={nums3}")
    print(f"Output: {solution.minSubArrayLen(target3, nums3)} (Expected: 0)\n")
    
    # 测试用例 4：用来揭示最初“碰撞指针”错误解法的反例
    target4, nums4 = 7, [5, 1, 3, 4, 2, 1, 1]
    print(f"Test 4 (Counter-example): target={target4}, nums={nums4}")
    print(f"Output: {solution.minSubArrayLen(target4, nums4)} (Expected: 2, sub-array [3, 4])\n")
