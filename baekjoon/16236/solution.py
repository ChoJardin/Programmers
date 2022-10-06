// [문제 링크]: https://www.acmicpc.net/problem/16236

from collections import deque
​
​
def find_shark():
    global N
​
    for i in range(N):
        for j in range(N):
            if ocean[i][j] == 9:
                return (i, j)
​
​
def move(y, x):
    global N, baby, baby_size
​
    # 상하좌우
    dy = [-1, +1, 0, 0]
    dx = [0, 0, -1, +1]
​
    eatable = []
    cur_move = 9999999999
​
    visited = [[False for _ in range(N)] for _ in range(N)]
​
    queue = deque()
    queue.append(((y, x), 0))
    visited[y][x] = True
​
    while queue:
        (y, x), now_cnt = queue.popleft()
​
        if now_cnt == cur_move:
            break
​
        for i in range(4):
            move_y = y + dy[i]
            move_x = x + dx[i]
​
            # 범위 체크, 이동 가능 확인,
            if -1 < move_y < N and -1 < move_x < N and not visited[move_y][move_x]:
​
                # 그냥 바다 혹은 크기 같은 물고기 > 이동 가능
                if not ocean[move_y][move_x] or ocean[move_y][move_x] == baby_size:
                    queue.append(((move_y, move_x), now_cnt + 1))
                    visited[move_y][move_x] = True
​
                # 먹을 수 있는 물고기
                elif ocean[move_y][move_x] < baby_size:
                    eatable.append([move_y, move_x])
                    cur_move = now_cnt+1
​
    return eatable, cur_move
​
​
N = int(input())
ocean = [list(map(int, input().split())) for _ in range(N)]
​
# 아기 상어 크기
baby = find_shark()
baby_size = 2
have_eaten = 0
​
cnt = 0
​
while True:
    eatable_fish, moved = move(baby[0], baby[1])
​
    if not eatable_fish:
        break
​
    # 물고기 자리 바다로 만들고
    ocean[baby[0]][baby[1]] = 0
​
    # 이동시킴
    baby = sorted(eatable_fish)[0]
​
    # 먹음
    ocean[baby[0]][baby[1]] = 9
​
    have_eaten += 1
    if have_eaten == baby_size:
        baby_size += 1
        have_eaten = 0
    cnt += moved
​
print(cnt)
​