class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]  # memoização

        # direções: cima, baixo, esquerda, direita
        direcoes = [(-1,0), (1,0), (0,-1), (0,1)]

        def dfs(i, j):
            # se já calculamos, retorna
            if dp[i][j] != 0:
                return dp[i][j]

            max_caminho = 1  # pelo menos a própria célula conta
            for dx, dy in direcoes:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    max_caminho = max(max_caminho, 1 + dfs(x, y))

            dp[i][j] = max_caminho
            return max_caminho

        # percorre toda a matriz
        resultado = 0
        for i in range(m):
            for j in range(n):
                resultado = max(resultado, dfs(i, j))

        return resultado
