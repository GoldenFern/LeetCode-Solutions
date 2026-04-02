import math

class Solution:
    """
    LeetCode 279: 完全平方数
    包含两种解法：动态规划法 和 数学定理法。
    主函数默认调用时间复杂度更优的数学定理法。
    """
    def numSquares(self, n: int) -> int:
        # 默认使用数学解法，时间复杂度 O(sqrt(n))
        return self.numSquares_math(n)

    def numSquares_math(self, n: int) -> int:
        """
        使用拉格朗日四平方和定理与勒让德三平方和定理
        """
        # 辅助函数：判断一个数是否为完全平方数
        def isPerfectSquare(x: int) -> bool:
            root = int(math.sqrt(x))
            return root * root == x

        # 1. 如果 n 本身是完全平方数，只需 1 个
        if isPerfectSquare(n):
            return 1
            
        # 2. 勒让德三平方和定理：判断 n 是否满足 4^a * (8b + 7)
        temp = n
        while temp % 4 == 0:
            temp //= 4  # 消除 4^a 因子
        if temp % 8 == 7:
            return 4    # 如果满足，必定需要 4 个平方数
            
        # 3. 判断是否可以由 2 个平方数组成
        # 枚举第一个平方数 i*i，看剩余部分 n - i*i 是否也是完全平方数
        for i in range(1, int(math.sqrt(n)) + 1):
            if isPerfectSquare(n - i * i):
                return 2
                
        # 4. 排除 1, 2, 4 的情况，根据四平方和定理，答案只能是 3
        return 3

    def numSquares_dp(self, n: int) -> int:
        """
        使用动态规划求解 (记录了我第二次尝试的正确思路)
        时间复杂度 O(n*sqrt(n))
        """
        # 易错点修正：使用一维数组而不是字典来记录状态
        dp = [float('inf')] * (n + 1)
        dp[0] = 0 # 核心基石：0需要0个平方数
        
        # 预先计算出所有可能的平方数，减少内层循环的重复计算
        max_square_index = int(math.sqrt(n)) + 1
        squares = [i * i for i in range(1, max_square_index)]
        
        # 易错点修正：双层循环，外层遍历所有数字，内层遍历平方数
        for i in range(1, n + 1):
            for square in squares:
                if i < square:
                    break # 剪枝：平方数大于当前数字，直接跳出
                # 状态转移：当前数字减去一个平方数后的最优解 + 1
                if dp[i - square] + 1 < dp[i]:
                    dp[i] = dp[i - square] + 1
                    
        return int(dp[n])

if __name__ == "__main__":
    sol = Solution()
    
    # 测试用例：(输入 n, 期望输出)
    test_cases = [
        (12, 3),     # 示例 1: 12 = 4 + 4 + 4
        (13, 2),     # 示例 2: 13 = 4 + 9
        (1, 1),      # 边界情况: 最小的完全平方数
        (4, 1),      # 完全平方数本身
        (7, 4),      # 满足 8b+7 的情况 (b=0)
        (28, 4),     # 满足 4^a(8b+7) 的情况: 28 = 4 * 7
        (43, 3),     # 答案为 3 的常规情况: 43 = 25 + 9 + 9
        (9999, 4)    # 较大数值测试
    ]
    
    for i, (n, expected) in enumerate(test_cases):
        # 同时测试两种方法，确保逻辑一致性
        res_math = sol.numSquares_math(n)
        res_dp = sol.numSquares_dp(n)
        
        print(f"Test Case {i+1}: n = {n}")
        print(f"  Expected = {expected}, Math Result = {res_math}, DP Result = {res_dp}")
        
        assert res_math == expected, f"Test Case {i+1} Math Failed!"
        assert res_dp == expected, f"Test Case {i+1} DP Failed!"
        
    print("\nAll test cases passed successfully!")
