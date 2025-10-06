
from typing import (
    List,
)
from collections import deque
class Solution:
    """
    number of island using dfs and bfs
    follow up: distrinct island: idea record original start position, for each move, calculate delta and
    input into a set and check final set size
    """
    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]
    def num_islands(self, grid: List[List[bool]]) -> int:
        # write your code here
        if not grid or not grid[0]:
            return 0
        row = len(grid)
        col = len(grid[0])
        vist = [[False] * col for _ in range(row)]
        count = 0
        for x in range(row):
            for y in range(col):
                if not vist[x][y] and grid[x][y]:
                    vist[x][y] = True
                    self.bfs(x, y, grid, vist)
                    count += 1
        return count

    def bfs(self, x: int, y: int, grid: List[List[bool]], vist: List[List[bool]]) -> None:
        qx = deque()
        qy = deque()
        qx.append(x)
        qy.append(y)
        vist[x][y] = True
        while len(qx) > 0:
            cx = qx.popleft()
            cy = qy.popleft()
            for i in range(4):
                nx = cx + self.dx[i]
                ny = cy + self.dy[i]
                if self.inbound(nx, ny, grid) and not vist[nx][ny] and grid[nx][ny]:
                    vist[nx][ny] = True
                    qx.append(nx)
                    qy.append(ny)
    def inbound(self, x: int, y: int, grid: List[List[bool]]):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])


from typing import (
    List,
)

class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    def num_islands(self, grid: List[List[bool]]) -> int:
        # write your code here
        if not grid or not grid[0]:
            return 0
        
        row, col = len(grid), len(grid[0])
        vist = [[False] * col for _ in range(row)]
        count = 0
        for i in range(row):
            for j in range(col):
                if not vist[i][j] and grid[i][j]:
                    vist[i][j] = True
                    self.dfs(i, j, grid, vist)
                    count += 1
        return count

    def dfs(self, x:int, y:int, grid:List[List[bool]], vist:List[List[bool]]) -> None:
        for i in range(4):
            nx = x + self.dx[i]
            ny = y + self.dy[i]
            if self.inbound(nx, ny, grid) and not vist[nx][ny] and grid[nx][ny]:
                vist[nx][ny] = True
                self.dfs(nx, ny, grid, vist)     
        
    def inbound(self, x:int, y:int, grid:List[List[bool]]) -> bool:
        row, col = len(grid), len(grid[0])
        return 0 <= x and x < row and 0 <= y and y < col