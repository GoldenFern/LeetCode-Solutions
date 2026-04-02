from collections import Counter
from typing import List

class Solution:
    """
    LeetCode 438: 找到字符串中所有字母异位词
    使用定长滑动窗口 + 哈希表 (Counter) 求解。
    """
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len, p_len = len(s), len(p)
        
        # 边界情况：如果 s 比 p 短，不可能有异位词
        if s_len < p_len:
            return []
            
        res = []
        p_count = Counter(p)
        window_count = Counter()
    
        # 初始化窗口：将前 p_len - 1 个字符的数据存入
        # 这样在进入主循环时，只需再加 1 个字符就能凑齐 p_len 长度
        for i in range(p_len - 1):
            window_count[s[i]] += 1

        # 开始滑动，i 为窗口的右边界
        for i in range(p_len - 1, s_len):
            # 1. 右边界字符进入窗口
            window_count[s[i]] += 1
            
            # 2. 比较当前窗口和目标频率是否一致
            # 注意：Python 3.10+ 中，Counter 比较会自动忽略值为 0 的键
            if window_count == p_count:
                res.append(i - p_len + 1)
            
            # 3. 左边界字符移出窗口，为下一次滑动做准备
            left_char = s[i - p_len + 1]
            window_count[left_char] -= 1
            
            # 兼容低版本 Python 的稳健写法（可选）：
            # 如果在 Python 3.9 及以下版本运行，必须加上下面两行代码
            # if window_count[left_char] == 0:
            #     del window_count[left_char]
                
        return res

if __name__ == "__main__":
    sol = Solution()
    
    # 定义测试用例
    test_cases = [
        ("cbaebabacd", "abc", [0, 6]),    # 示例 1
        ("abab", "ab", [0, 1, 2]),        # 示例 2
        ("a", "a", [0]),                  # 边界：长度相等且相同
        ("a", "ab", []),                  # 边界：s 比 p 短
        ("baa", "aa", [1]),               # 易错：包含重复字符的异位词
        ("abc", "def", [])                # 边界：完全不匹配
    ]
    
    for i, (s, p, expected) in enumerate(test_cases):
        result = sol.findAnagrams(s, p)
        print(f"Test Case {i+1}: s='{s}', p='{p}'")
        print(f"  Expected = {expected}, Result = {result}")
        assert result == expected, f"Test Case {i+1} Failed!"
        
    print("\nAll test cases passed successfully!")
