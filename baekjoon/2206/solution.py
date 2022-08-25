// [문제 링크]: https://www.acmicpc.net/problem/2206

from collections import deque
​
def bfs():
    global min_cnt
​
    # 상하좌우
    dy = [-1, +1, 0, 0]
    dx = [0, 0, -1, +1]
​
    # 현재 좌표, 방문 기록, 벽 부쉈나, 몇번 이동했나
    queue = deque()
​
    queue.append(((0, 0), False, 1))
    visited[0][0][False] = 1
​
    while queue:
        (y, x), is_broken, cnt = queue.popleft()
​
        for i in range(4):
            move_y = y + dy[i]
            move_x = x + dx[i]
​
            # 범위 확인 && 방문확인
            if -1 < move_y < N and -1 < move_x < M:
​
                # 이동 가능 여부 확인
                # 벽이지만 아직 부술 수 있다면?
                if board[move_y][move_x]:
                    if not is_broken and visited[move_y][move_x][True] > cnt+1:
                        # 부수고 이동
                        queue.append(((move_y, move_x), True, cnt+1))
                        visited[move_y][move_x][True] = cnt+1
​
                # 벽이 아니어서 이동 가능한 경우
                else:
                    if visited[move_y][move_x][is_broken] > cnt+1:
                        queue.append(((move_y, move_x), is_broken, cnt+1))
                        visited[move_y][move_x][is_broken] = cnt+1
​
    # 끝까지 오지 못했음
    return -1
​
​
# 지도 크기
N, M = map(int, input().split())
​
# 지도
board = [list(map(int, list(input()))) for _ in range(N)]
​
visited = [[{True: 999999999, False: 999999999} for _ in range(M)] for __ in range(N)]
​
bfs()
​
min_cnt = min(visited[N-1][M-1].values())
​
if min_cnt != 999999999:
    print(min_cnt)
else:
    print(-1)
​
​