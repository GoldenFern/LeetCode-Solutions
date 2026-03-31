from typing import List

class Solution:
    """
    包含 LeetCode 283 (移动零) 和 15 (三数之和) 的解决方案
    """

    def moveZeroes(self, nums: List[int]) -> None:
        """
        LeetCode 283: 移动零
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        # fast 指针遍历数组寻找非零元素
        for fast in range(len(nums)):
            if nums[fast] != 0:
                # 遇到非零元素，将其与 slow 指向的位置交换，并推进 slow
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        LeetCode 15: 三数之和
        """
        # 1. 排序是双指针和去重的基础
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n - 2):
            # 剪枝：如果排序后第一个数已经大于0，后面不可能凑成和为0
            if nums[i] > 0:
                break
            
            # 外层去重：跳过重复的第一个数 (注意要保证 i > 0 避免越界)
            # 必须是和 i-1 比较，代表当前数字是否已经被作为第一个数枚举过
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # 初始化双指针
            left = i + 1
            right = n - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    # 和太小，左指针右移寻找更大的数
                    left += 1
                elif total > 0:
                    # 和太大，右指针左移寻找更小的数
                    right -= 1
                else:
                    # 找到一个和为0的三元组
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # 内层去重：跳过重复的第二个数 (左指针指向的数)
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # 内层去重：跳过重复的第三个数 (右指针指向的数)
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # 找到一个答案并去重后，双指针同时往中间收缩，继续寻找下一组
                    left += 1
                    right -= 1
                    
        return res

if __name__ == "__main__":
    sol = Solution()

    print("--- Testing LeetCode 283: Move Zeroes ---")
    test_cases_283 = [
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([0], [0]),
        ([1, 2, 3], [1, 2, 3]), # 无零情况
        ([0, 0, 0], [0, 0, 0])  # 全零情况
    ]
    for i, (nums_in, expected) in enumerate(test_cases_283):
        # 复制一份用于打印，因为函数是原地修改
        original = nums_in.copy() 
        sol.moveZeroes(nums_in)
        print(f"Test Case {i+1}: Input = {original}")
        print(f"  Expected = {expected}, Result = {nums_in}")
        assert nums_in == expected, f"LC 283 Test Case {i+1} Failed!"
    print("LC 283 All test cases passed successfully!\n")


    print("--- Testing LeetCode 15: 3Sum ---")
    test_cases_15 = [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]), # 示例 1
        ([0, 1, 1], []),                                    # 示例 2
        ([0, 0, 0], [[0, 0, 0]]),                           # 示例 3
        ([0, 0, 0, 0], [[0, 0, 0]]),                        # 边界：多个0去重测试
        ([-2, 0, 0, 2, 2], [[-2, 0, 2]])                    # 边界：双指针去重测试
    ]
    for i, (nums_in, expected) in enumerate(test_cases_15):
        result = sol.threeSum(nums_in)
        print(f"Test Case {i+1}: Input = {nums_in}")
        print(f"  Expected = {expected}, Result = {result}")
        assert result == expected, f"LC 15 Test Case {i+1} Failed!"
    print("LC 15 All test cases passed successfully!")
