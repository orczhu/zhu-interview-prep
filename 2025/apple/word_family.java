// word search

public class Solution {
    /**
     * @param board: A list of lists of character
     * @param word: A string
     * @return: A boolean
     */
    int[] dx = {0, -1, 0, 1};
    int[] dy = {1, 0, -1, 0};
    public boolean exist(char[][] A, String word) {
        // write your code here
        if (A == null || A.length == 0 || A[0] == null || A[0].length == 0) {
            return false;
        }
        int row = A.length;
        int col = A[0].length;
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (A[i][j] == word.charAt(0)) {
                    boolean[][] vist = new boolean[row][col];
                    vist[i][j] = true;
                    boolean isFound = dfs(A, vist, i, j, word, 1);
                    if (isFound) {
                        return true;
                    }
                }
            }
        }
        return false;
    }

    private boolean dfs(char[][] A, boolean[][] vist, int x, int y, String word, int level) {
        if (level == word.length()) {
            return true;
        }
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (inBound(nx, ny, A) && !vist[nx][ny] && A[nx][ny] == word.charAt(level)) {
                vist[nx][ny] = true;
                if (dfs(A, vist, nx, ny, word, level + 1)) {
                    return true;
                }
                vist[nx][ny] = false;
            }
        }
        return false;
    }

    private boolean inBound(int x, int y, char[][] A) {
        return 0 <= x && x < A.length && 0 <=y && y < A[0].length;
    }
}