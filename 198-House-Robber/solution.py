from typing import List

class Solution:
    """
    LeetCode 198: 打家劫舍
    使用动态规划 (Dynamic Programming) 求解，空间复杂度优化至 O(1)。
    """
    def rob(self, nums: List[int]) -> int:
        room_total = len(nums)
        
        # 边界情况处理
        if room_total == 0:
            return 0
        if room_total == 1:
            return nums[0]
        if room_total == 2:
            return max(nums[0], nums[1])

        # 初始化状态
        # f_n_minus_2 代表 f(n-2)
        # f_n_minus_1 代表 f(n-1)
        f_n_minus_2 = nums[0]
        f_n_minus_1 = max(nums[0], nums[1])
        
        # 从第三间房开始遍历
        for i in range(2, room_total):
            # 状态转移方程: f(n) = max(f(n-1), f(n-2) + nums[i])
            current_f = max(f_n_minus_1, f_n_minus_2 + nums[i])
            
            # 更新状态变量
            # 注意：必须先更新 f_n_minus_2，或者使用 Python 的并行赋值
            f_n_minus_2 = f_n_minus_1
            f_n_minus_1 = current_f
            
        return f_n_minus_1

if __name__ == "__main__":
    sol = Solution()
    
    # 测试用例
    test_cases = [
        ([1, 2, 3, 1], 4),       # 示例 1: 1+3=4
        ([2, 7, 9, 3, 1], 12),    # 示例 2: 2+9+1=12
        ([0], 0),                # 边界: 只有一间房且金额为0
        ([2, 1], 2),             # 边界: 两间房，第一间大
        ([1, 2], 2),             # 边界: 两间房，第二间大
        ([2, 1, 1, 2], 4)        # 进阶: 2+2=4
    ]
    
    for i, (nums, expected) in enumerate(test_cases):
        result = sol.rob(nums)
        print(f"Test Case {i+1}: Input = {nums}")
        print(f"  Expected = {expected}, Result = {result}")
        assert result == expected, f"Test Case {i+1} Failed!"
    
    print("\nAll test cases passed successfully!")
