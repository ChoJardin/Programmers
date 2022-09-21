// [문제 링크]: https://www.acmicpc.net/problem/10026

from collections import deque
​
def bfs(v, is_blue_only):    
    global N, paint, visited
​
    if is_blue_only:
        cur_visited = visited[1]
    else:
        cur_visited = visited[0]
​
    # 사방탐색
    dy = [-1, +1, 0, 0]
    dx = [0, 0, -1, +1]
​
    queue = deque()
​
    # 현재 위치,
    queue.append((v[0], v[1]))
    # 방문체크
    cur_visited[v[0]][v[1]] = True
​
    while queue:
        cur_y, cur_x = queue.popleft()
​
        # 사방탐색
        for i in range(4):
            move_y = cur_y + dy[i]
            move_x = cur_x + dx[i]
​
            # 범위 확인, 아직 방문 안 함
            if -1 < move_y < N and -1 < move_x < N and not cur_visited[move_y][move_x]:
                # 적록색약
                if is_blue_only:
                    # 파랑-파랑 이거나 아니거나
                    if paint[cur_y][cur_x] == 'B' and paint[move_y][move_x] == 'B':
                        queue.append((move_y, move_x))
                        cur_visited[move_y][move_x] = True
​
                    elif paint[cur_y][cur_x] != 'B' and paint[move_y][move_x] != 'B':
                        queue.append((move_y, move_x))
                        cur_visited[move_y][move_x] = True
​
                else:
                    if paint[cur_y][cur_x] == paint[move_y][move_x]:
                        queue.append((move_y, move_x))
                        cur_visited[move_y][move_x] = True
​
​
N = int(input())
​
paint = [list(input()) for _ in range(N)]
​
visited = [[[False for _ in range(N)] for _ in range(N)], [[False for _ in range(N)] for _ in range(N)]]
​
cnt = [0, 0]
​
for i in range(N):
    for j in range(N):
​
        if not visited[0][i][j]:
            bfs((i, j), False)
            cnt[0] += 1
​
        if not visited[1][i][j]:
            bfs((i, j), True)
            cnt[1] += 1
​
print(*cnt)