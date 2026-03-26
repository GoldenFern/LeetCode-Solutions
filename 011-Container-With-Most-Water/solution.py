class Solution:
    """
    LeetCode 11: 盛最多水的容器
    使用双指针 (Two Pointers) 算法求解。
    """
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            # 获取当前的左右边界高度
            h_left = height[left]
            h_right = height[right]

            # 计算当前面积并更新最大值
            # 避免使用内置的 min 函数，在紧凑循环中略微提升性能
            current_height = h_left if h_left < h_right else h_right
            current_area = current_height * (right - left)
            
            if current_area > max_area:
                max_area = current_area

            # 优化：移动指针时，跳过所有比当前边界矮或等高的位置
            # 因为宽度在减小，只有高度增加才有可能得到更大的面积
            if h_left < h_right:
                while left < right and height[left] <= h_left:
                    left += 1
            else:
                while left < right and height[right] <= h_right:
                    right -= 1

        return max_area

if __name__ == "__main__":
    sol = Solution()
    
    # 测试用例：(输入数组, 期望最大面积)
    test_cases = [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49), # 示例 1
        ([1, 1], 1),                       # 示例 2
        ([4, 3, 2, 1, 4], 16),             # 两端高，中间低
        ([1, 2, 1], 2),                    # 中间高，两端低
        ([2, 3, 4, 5, 18, 17, 6], 17)      # 最优解在内部
    ]
    
    for i, (test_input, expected_output) in enumerate(test_cases):
        result = sol.maxArea(test_input)
        print(f"Test Case {i+1}: Input = {test_input}")
        print(f"  Expected = {expected_output}, Result = {result}")
        assert result == expected_output, f"Test Case {i+1} Failed!"
    
    print("\nAll test cases passed successfully!")
