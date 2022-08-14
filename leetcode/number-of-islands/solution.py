// [문제 링크]: https://leetcode.com/problems/number-of-islands/submissions/

from collections import deque

class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # 방문체크
        visited = [[False for i in range(n)] for j in range(m)]

        # 상하좌우
        dy = [-1, +1, 0, 0]
        dx = [0, 0, -1, +1]

        # 섬 개수 확인
        cnt = 0

        queue = deque()

        for i in range(m):
            for j in range(n):

                if grid[i][j] == '1' and not visited[i][j]:
                    queue.append((i, j))
                    
                    while queue: 
                        
                        current_y, current_x = queue.popleft()
                        
                        for k in range(4): 
                                
                            move_y = current_y + dy[k]
                            move_x = current_x + dx[k] 
                            
                            if -1 < move_y < m and -1 < move_x < n and not visited[move_y][move_x] and grid[move_y][move_x] == '1': 
                                queue.append((move_y, move_x))
                                visited[move_y][move_x] = True 
                    
                    cnt += 1 
        
        return cnt

