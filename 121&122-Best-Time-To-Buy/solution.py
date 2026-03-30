from typing import List

class Solution:
    # ==========================================
    # LeetCode 121: 只能交易一次
    # ==========================================
    def maxProfit_121_greedy(self, prices: List[int]) -> int:
        """
        121题：贪心/单向遍历
        时间 O(N), 空间 O(1)
        """
        min_price = float('inf') # 历史最低价格
        max_profit = 0           # 当前最大利润
        
        for price in prices:
            # 更新历史最低价格
            min_price = min(min_price, price)
            # 计算如果今天卖出的利润，并更新最大利润
            max_profit = max(max_profit, price - min_price)
            
        return max_profit

    def maxProfit_121_dp(self, prices: List[int]) -> int:
        """
        121题：动态规划 (空间优化版)
        时间 O(N), 空间 O(1)
        """
        if not prices: return 0
        cash = 0          # 不持股的最大利润
        hold = -prices[0] # 持股的最大利润 (因为只能买一次，买入前利润必为0)
        
        for i in range(1, len(prices)):
            cash = max(cash, hold + prices[i])
            # 注意这里与 122 题的区别：买入时直接是 -prices[i]
            hold = max(hold, -prices[i]) 
            
        return cash

    # ==========================================
    # LeetCode 122: 可以交易无数次
    # ==========================================
    def maxProfit_122_dp(self, prices: List[int]) -> int:
        """
        122题：动态规划 (空间优化版)
        时间 O(N), 空间 O(1)
        """
        if not prices: return 0
        cash = 0          # 对应 dp[n][0]
        hold = -prices[0] # 对应 dp[n][1]
        
        for i in range(1, len(prices)):
            # 记录昨天的 cash，防止在更新 hold 时被覆盖
            prev_cash = cash
            # 今天不持股 = max(昨天不持股, 昨天持股今天卖出)
            cash = max(cash, hold + prices[i])
            # 今天持股 = max(昨天持股, 昨天不持股今天买入)
            hold = max(hold, prev_cash - prices[i])
            
        return cash

    def maxProfit_122_greedy(self, prices: List[int]) -> int:
        """
        122题：贪心算法
        时间 O(N), 空间 O(1)
        """
        profit = 0
        for i in range(1, len(prices)):
            # 只要今天比昨天价格高，就收集这段利润
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit


if __name__ == "__main__":
    sol = Solution()
    
    # 测试用例格式: (股票价格数组, 121题期望结果, 122题期望结果)
    test_cases = [
        ([7, 1, 5, 3, 6, 4], 5, 7),  # 常规波动
        ([1, 2, 3, 4, 5], 4, 4),     # 单调递增
        ([7, 6, 4, 3, 1], 0, 0),     # 单调递减
        ([2, 4, 1], 2, 2),           # 只有一次上涨机会
        ([3, 2, 6, 5, 0, 3], 4, 7)   # 复杂波动
    ]
    
    print("Running Tests for LeetCode 121 & 122...\n")
    
    for i, (prices, exp_121, exp_122) in enumerate(test_cases):
        # 测试 121 题
        res_121_greedy = sol.maxProfit_121_greedy(prices)
        res_121_dp = sol.maxProfit_121_dp(prices)
        assert res_121_greedy == res_121_dp == exp_121, f"Test Case {i+1} for LC 121 Failed!"
        
        # 测试 122 题
        res_122_dp = sol.maxProfit_122_dp(prices)
        res_122_greedy = sol.maxProfit_122_greedy(prices)
        assert res_122_dp == res_122_greedy == exp_122, f"Test Case {i+1} for LC 122 Failed!"
        
        print(f"Test Case {i+1} Passed! Prices: {prices}")
        print(f"  LC 121 Max Profit: {exp_121}")
        print(f"  LC 122 Max Profit: {exp_122}\n")
        
    print("All test cases passed successfully!")
