class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        '''brute force approach 
        class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:

        # dimensions
        rows = len(mat)
        cols = len(mat[0])

        # answer matrix
        ans = [[0] * cols for _ in range(rows)]

        # traverse every cell
        for i in range(rows):
            for j in range(cols):
                total = 0

                # calculate boundaries
                row_start = max(0, i - k)
                row_end = min(rows - 1, i + k)

                col_start = max(0, j - k)
                col_end = min(cols - 1, j + k)

                # calculate block sum
                for r in range(row_start, row_end + 1):
                    for c in range(col_start, col_end + 1):
                        total += mat[r][c]

                # store answer
                ans[i][j] = total

        return ans
        time complexity ->o(m^2n^2)
        space complexity->o(mn)
repeated work for optimization:->Agar matrix:

100 × 100

hai aur k bada hai, to har cell ka block bahut bada hoga.

Ek cell ke liye hum hundreds/thousands of elements add karenge.

Next cell ke liye unhi elements ka bada portion phir se add karenge.

Next cell → phir.

Next cell → phir.

That's the repeated work.
        '''
        rows = len(mat)
        cols = len(mat[0])

        # 2D Prefix Sum
        prefix = [[0] * (cols + 1) for _ in range(rows + 1)]

        for i in range(rows):
            for j in range(cols):
                prefix[i + 1][j + 1] = (
                    mat[i][j]
                    + prefix[i][j + 1]
                    + prefix[i + 1][j]
                    - prefix[i][j]
                )

        ans = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):

                r1 = max(0, i - k)
                c1 = max(0, j - k)

                r2 = min(rows - 1, i + k)
                c2 = min(cols - 1, j + k)

                # Rectangle sum using prefix sum
                ans[i][j] = (
                    prefix[r2 + 1][c2 + 1]
                    - prefix[r1][c2 + 1]
                    - prefix[r2 + 1][c1]
                    + prefix[r1][c1]
                )

        return ans
        