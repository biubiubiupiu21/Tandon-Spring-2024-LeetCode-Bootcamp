class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        memo = [[0] * n for _ in range(m)]

        def dfs(x, y):
            if memo[x][y] != 0:
                return memo[x][y]
            
            # Directions for moving in the matrix (left, right, up, down)
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            max_path = 1  # Minimum path length is 1 (just the cell itself)
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] > matrix[x][y]:
                    max_path = max(max_path, 1 + dfs(nx, ny))
            
            memo[x][y] = max_path
            return memo[x][y]

        longest = 0
        # Compute the longest increasing path starting from each cell
        for i in range(m):
            for j in range(n):
                longest = max(longest, dfs(i, j))
        
        return longest