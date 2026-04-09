from typing import List
from collections import defaultdict

class Solution:
    """
    LeetCode 49: 字母异位词分组
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # --- 错误思路展示 (Failed Attempt) ---
        # result = {}
        # for s in strs:
        #     s_set = frozenset(s) # 错误：frozenset 会丢弃字符出现的次数
        #     # 如果输入 ["ddddddddddg", "dgggggggggg"]
        #     # 它们的 frozenset 都是 {'d', 'g'}，会被错误地归为一类
        # -----------------------------------

        # --- 正确思路：排序法 ---
        # key: 排序后的字符串 (唯一标识), value: 原始字符串列表
        anagram_map = defaultdict(list)
        
        for s in strs:
            # 1. 排序：将 "eat" 变为 ['a', 'e', 't']
            # 2. 序列化：将列表转回字符串 "aet" 作为不可变的 key
            sorted_key = "".join(sorted(s))
            
            # 3. 归类
            anagram_map[sorted_key].append(s)
            
        return list(anagram_map.values())

if __name__ == "__main__":
    sol = Solution()
    
    # 测试用例 1: 常规情况
    case1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    # 测试用例 2: 易错点（frozenset 会失败的情况）
    case2 = ["ddddddddddg", "dgggggggggg"]
    
    print("Testing Case 1...")
    res1 = sol.groupAnagrams(case1)
    print(f"Result: {res1}")
    # 验证长度是否正确
    assert len(res1) == 3

    print("\nTesting Case 2 (Frequency Check)...")
    res2 = sol.groupAnagrams(case2)
    print(f"Input: {case2}")
    print(f"Result: {res2}")
    # 如果使用了 frozenset，这里的长度会是 1，导致断言失败
    assert len(res2) == 2, "Failed: 'ddddddddddg' and 'dgggggggggg' are NOT anagrams!"
    
    print("\nAll test cases passed!")
