class Solution:
    """
    包含 LeetCode 70: 爬楼梯 和 经典 0-1 背包问题的解决方案。
    """
    
    def climbStairs(self, n: int) -> int:
        """
        LeetCode 70: 爬楼梯
        使用空间优化的动态规划（滚动变量）求解，时间复杂度 O(n)，空间复杂度 O(1)。
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        
        # 初始状态：f(1) = 1, f(2) = 2
        f_k_minus_2 = 1
        f_k_minus_1 = 2
        
        # 从 n=3 开始迭代计算
        for _ in range(3, n + 1):
            f_k = f_k_minus_1 + f_k_minus_2
            # 滚动更新变量，为下一次迭代做准备
            f_k_minus_2 = f_k_minus_1
            f_k_minus_1 = f_k
            
        return f_k

    def knapsack01(self, weights: list[int], values: list[int], capacity: int) -> int:
        """
        经典 0-1 背包问题
        使用一维数组进行空间优化的动态规划求解。
        
        :param weights: 物品的重量列表
        :param values: 物品的价值列表
        :param capacity: 背包的最大承重
        :return: 背包能装入的最大价值
        """
        n = len(weights)
        # dp[j] 表示容量为 j 的背包所能装入的最大价值
        # 初始化为 0
        dp = [0] * (capacity + 1)
        
        # 遍历每一个物品
        for i in range(n):
            w = weights[i]
            v = values[i]
            # 必须从后向前遍历背包容量，防止当前物品被重复放入（即变成完全背包）
            for j in range(capacity, w - 1, -1):
                dp[j] = max(dp[j], dp[j - w] + v)
                
        return dp[capacity]

if __name__ == "__main__":
    sol = Solution()
    
    # ==========================================
    # 测试 LeetCode 70: 爬楼梯
    # ==========================================
    print("--- Testing Climbing Stairs ---")
    stair_test_cases = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 5),
        (5, 8),
        (38, 39088169) # 较大的数，验证效率
    ]
    
    for i, (n, expected) in enumerate(stair_test_cases):
        result = sol.climbStairs(n)
        print(f"Test Case {i+1}: n = {n}, Expected = {expected}, Result = {result}")
        assert result == expected, f"Climbing Stairs Test Case {i+1} Failed!"
    print("All Climbing Stairs tests passed!\n")
    
    # ==========================================
    # 测试 0-1 背包问题
    # ==========================================
    print("--- Testing 0-1 Knapsack ---")
    knapsack_test_cases = [
        # (weights, values, capacity, expected_max_value)
        ([1, 2, 3], [6, 10, 12], 5, 22), # 选重量2和3，价值10+12=22
        ([2, 2, 6, 5, 4], [6, 3, 5, 4, 6], 10, 15), # 选重量2,2,4，价值6+3+6=15
        ([10, 20, 30], [60, 100, 120], 50, 220) # 选重量20+30，价值100+120=220
    ]
    
    for i, (w, v, cap, expected) in enumerate(knapsack_test_cases):
        result = sol.knapsack01(w, v, cap)
        print(f"Test Case {i+1}: capacity = {cap}, Expected = {expected}, Result = {result}")
        assert result == expected, f"Knapsack Test Case {i+1} Failed!"
    print("All 0-1 Knapsack tests passed!")
