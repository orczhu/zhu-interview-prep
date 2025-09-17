// Good one could be BFS or DFS for number of islands
// Dfs solution
public class Solution {
    /**
     * @param grid: a boolean 2D matrix
     * @return: an integer
     */
    int dx[] = {0, 1, 0, -1};
    int dy[] = {1, 0, -1, 0};
    public int numIslands(boolean[][] A) {
        // write your code here
        // dfs
        if (A == null ||A.length == 0 || A[0] == null || A[0].length == 0) {
            return 0;
        }
        int row = A.length;
        int col = A[0].length;
        int count = 0;
        boolean[][] vist = new boolean[row][col];
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (vist[i][j] || !A[i][j]) {
                    continue;
                }
                vist[i][j] = true;
                dfs(i, j, row, col, vist, A);
                count++;
            }
        }
        return count;
    }
    private void dfs(int x, int y, int row, int col, boolean[][] vist, boolean[][] A) {
        for (int i = 0; i < 4; i++) {
            int xn = x + dx[i];
            int yn = y + dy[i];
            if (xn >= 0 && xn < row && yn < col && yn >= 0 && !vist[xn][yn] && A[xn][yn]) {
                vist[xn][yn] = true;
                dfs(xn, yn, row, col, vist, A);
            }
        }
    }
}

// BFS solution 
