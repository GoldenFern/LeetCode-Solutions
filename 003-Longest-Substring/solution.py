class Solution:
    """
    LeetCode 3: 无重复字符的最长子串
    使用滑动窗口 (Sliding Window) 算法求解。
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 哈希表用于存储字符最后一次出现的索引: {char: index}
        char_map = {} 
        max_length = 0
        left = 0 # 滑动窗口的左边界

        # 遍历字符串，right 为窗口右边界
        for right, char in enumerate(s):
            # 如果字符在哈希表中出现过，说明可能在当前窗口内产生了重复
            if char in char_map:
                # 更新左边界。必须使用 max 防止 left 指针向左倒退（例如遇到 "abba" 的情况）
                left = max(left, char_map[char] + 1)
            
            # 计算当前窗口长度，并更新最大长度
            max_length = max(max_length, right - left + 1)
            
            # 更新当前字符在哈希表中的最新索引
            char_map[char] = right
            
        return max_length

if __name__ == "__main__":
    # 实例化解决方案类
    sol = Solution()
    
    # 定义测试用例：包含题目示例以及一些关键的边界情况
    # 格式: (输入字符串, 期望的输出长度)
    test_cases = [
        ("abcabcbb", 3),  # 示例 1: 常规情况
        ("bbbbb", 1),     # 示例 2: 全重复字符
        ("pwwkew", 3),    # 示例 3: 答案必须是子串 ("wke")，不能是子序列 ("pwke")
        ("", 0),          # 边界 1: 空字符串
        (" ", 1),         # 边界 2: 只包含一个空格
        ("au", 2),        # 边界 3: 只有两个不重复字符
        ("abba", 2)       # 易错点: 测试 left 指针是否会错误地向左回退
    ]
    
    # 批量执行测试
    for i, (test_input, expected_output) in enumerate(test_cases):
        result = sol.lengthOfLongestSubstring(test_input)
        print(f"Test Case {i+1}: Input = '{test_input}'")
        print(f"  Expected = {expected_output}, Result = {result}")
        
        # 使用 assert 进行断言，如果结果不符合预期，程序会报错并停止
        assert result == expected_output, f"Test Case {i+1} Failed!"
    
    print("\nAll test cases passed successfully!")