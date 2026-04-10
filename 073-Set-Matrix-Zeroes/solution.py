from typing import List

class Solution:
    """
    LeetCode 73: 矩阵置零
    使用 $O(1)$ 额外空间的标记法。
    """
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return
            
        m, n = len(matrix), len(matrix[0])
        
        # 1. 记录第一行和第一列原本是否包含 0
        first_row_has_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_has_zero = any(matrix[i][0] == 0 for i in range(m))
        
        # 2. 使用第一行和第一列作为标记数组 (从 1,1 开始遍历)
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # 3. 根据第一行和第一列的标记，将内部元素置 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # 4. 最后根据布尔变量处理第一行
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0
                
        # 5. 最后根据布尔变量处理第一列
        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0

if __name__ == "__main__":
    sol = Solution()
    
    # 测试用例 1: 常规矩阵
    case1 = [[1,1,1],[1,0,1],[1,1,1]]
    sol.setZeroes(case1)
    assert case1 == [[1,0,1],[0,0,0],[1,0,1]]
    
    # 测试用例 2: 包含多个 0 的矩阵
    case2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    sol.setZeroes(case2)
    assert case2 == [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
    
    # 测试用例 3: 第一行第一列本身有 0
    case3 = [[1,0,3]]
    sol.setZeroes(case3)
    assert case3 == [[0,0,0]]
    
    # 测试用例 4: 单个元素
    case4 = [[1]]
    sol.setZeroes(case4)
    assert case4 == [[1]]
    
    case5 = [[0]]
    sol.setZeroes(case5)
    assert case5 == [[0]]

    print("All test cases passed!")
