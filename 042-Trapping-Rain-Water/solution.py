from typing import List

class Solution:
    """
    LeetCode 42: 接雨水
    使用双指针法 (Two Pointers) 求解，时间复杂度 O(N)，空间复杂度 O(1)。
    """
    def trap(self, height: List[int]) -> int:
        # 边界情况：如果数组为空或长度小于3，无法形成凹槽接水
        if not height or len(height) < 3:
            return 0
            
        left = 0
        right = len(height) - 1
        
        left_max = 0
        right_max = 0
        total_water = 0
        
        # 双指针向中间逼近
        while left < right:
            # 如果左侧柱子低于右侧柱子，说明左侧的短板效应已经确定
            if height[left] < height[right]:
                # 更新左侧历史最高
                left_max = max(left_max, height[left])
                # 当前柱子能接的水 = 左侧最高 - 当前柱子高度
                # (如果当前柱子就是最高，相减为0，不会出现负数)
                total_water += (left_max - height[left])
                left += 1
            else:
                # 如果右侧柱子低于或等于左侧柱子，说明右侧的短板效应已经确定
                right_max = max(right_max, height[right])
                # 当前柱子能接的水 = 右侧最高 - 当前柱子高度
                total_water += (right_max - height[right])
                right -= 1
                
        return total_water

if __name__ == "__main__":
    sol = Solution()
    
    # 测试用例设计
    test_cases = [
        ([0,1,0,2,1,0,1,3,2,1,2,1], 6),  # 示例 1: 常规凹凸不平
        ([4,2,0,3,2,5], 9),              # 示例 2: 另一组常规测试
        ([1, 2, 3, 4, 5], 0),            # 边界 1: 单调递增，无法接水
        ([5, 4, 3, 2, 1], 0),            # 边界 2: 单调递减，无法接水
        ([1, 3, 1], 0),                  # 边界 3: 凸字形 (金字塔)，无法接水
        ([3, 1, 3], 2),                  # 边界 4: 凹字形 (山谷)，接水2个单位
        ([0], 0),                        # 边界 5: 只有一个柱子
        ([], 0)                          # 边界 6: 空数组
    ]
    
    for i, (height, expected) in enumerate(test_cases):
        result = sol.trap(height)
        print(f"Test Case {i+1}: Input = {height}")
        print(f"  Expected = {expected}, Result = {result}")
        assert result == expected, f"Test Case {i+1} Failed!"
        
    print("\nAll test cases passed successfully!")
