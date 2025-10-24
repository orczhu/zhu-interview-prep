# Word search dfs n^4
from typing import (
    List,
)

class Solution:
    """
    @param board: A list of lists of character
    @param word: A string
    @return: A boolean
    """
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    def exist(self, board: List[List[str]], word: str) -> bool:
        # write your code here
        if not board:
            return False

        row = len(board)
        col = len(board[0])
        result = False
        for i in range(row):
            for j in range(col):
                if board[i][j] != word[0]:
                    continue
                vist = set()
                
                result = result or self.dfs(board, word, i, j, 0, vist)
        return result
    
    def dfs(self, board, word, x, y, level, vist):
        if level >= len(word):
            return False
        
        if board[x][y] != word[level]:
            return False

        if level == len(word) - 1:
            return True

        if (x, y) in vist:
            return False
        vist.add((x, y))
        for i in range(4):
            next_x = x + self.dx[i]
            next_y = y + self.dy[i]
            if self.is_in_bound(board, next_x, next_y) and (next_x, next_y) not in vist:
                if self.dfs(board, word, next_x, next_y, level + 1, vist):
                    return True
        vist.remove((x, y))
        return False
    
    def is_in_bound(self, grid, x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])

## Word search II
# Using prefix to remove dupliate search
from typing import (
    List,
)

class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
             we will sort your return value in output
    """
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    def word_search_i_i(self, board: List[List[str]], words: List[str]) -> List[str]:
        # write your code here
        if not board:
            return []
        prefix_set = self.get_prefix(words)
        print(prefix_set)
        row = len(board)
        col = len(board[0])
        result = set()
        for x in range(row):
            for y in range(col):
                if board[x][y] in prefix_set:
                    current = [board[x][y]]
                    self.dfs(x, y, prefix_set, words, board, set([(x, y)]), result, current)
        
        return list(result)
    
    def get_prefix(self, words):
        result_set = set()
        for word in words:
            for i in range(1,len(word) + 1):
                result_set.add(word[:i])
        return list(result_set)

    def dfs(self, x, y, prefix_set, words, board, vist, result, current):
        if ''.join(current) not in prefix_set:
            return
        if ''.join(current) in words:
            result.add(''.join(current))

        for i in range(4):
            nx = x + self.dx[i]
            ny = y + self.dy[i]
            if self.in_bound(nx, ny, board) and (nx, ny) not in vist:
                current.append(board[nx][ny])
                vist.add((nx, ny))
                self.dfs(nx, ny, prefix_set, words, board, vist, result, current)
                vist.remove((nx, ny))
                current.pop()
    def in_bound(self, x, y, board):
        return 0 <= x < len(board) and 0 <= y < len(board[0])

