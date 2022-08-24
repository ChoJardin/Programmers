// [문제 링크]: https://www.acmicpc.net/problem/9663

# 퀸을 한줄씩 놓으면서 내려간다.
# 퀸을 놓을 때는? 이미 놓아있는 퀸들을 확인함
# 내 위치에서 놓을 수 없다면, 다음 자리를 확인하는 것
# 퀸의 이동 가능 범위: 가로/ 세로/ 대각선 <- 대각선은 위쪽에 이미 놓여있는 친구들만 확인하면 된다.
​
def put_queen(y):
    global cnt, N, dx, already_put
​
    # 퀸을 N개 모두 체스판에 놓았음
    if y == N:
        cnt += 1
        return
​
    # 상, 좌상, 우상 세가지만 확인하면 됨
    dx = [-1, +1]
​
    # 퀸을 체스 판에 놓아야 함
    # y 번째 줄에 퀸을 놓을 차례
    # 가로만 순회하면서 퀸 놓는 자리 확인해 주면된다
    for x in range(N):
        # 현재 위치: board[y][x]
​
        # x 가 놓여질 수 있는 위치인지의 확인을 해보자
        if already_put.__contains__(x):
            continue
​
        # 현재 위치에 놓을 수 있는지 먼저 확인한다
        # 위로 계속 올라가면서 확인해줘야 하는데 어찌했죠?
        # 아하 내가 현재 y 번째 이니까 y번만 확인해주면 되는 거였군요?
​
        for i in range(1, y+1):
​
            is_possible = True
​
            for j in range(2):
​
                move_y = y-i
                move_x = x+dx[j]*i
​
                # 범위 확인 && 이미 체스판을 놓았나
                if -1 < move_y < N and -1 < move_x < N and board[move_y][move_x]:
                    is_possible = False
                    break
​
            if not is_possible:
                break
​
        else:
            # 확인이 끝났음
            # 이 자리에 퀸 놓을 수 있다
            board[y][x] = True
            # 퀸 놓은 x 저장
            already_put.add(x)
​
            # 다음 줄 확인하러 가자
            put_queen(y+1)
​
            # 돌아왔으니 퀸 다시 없애준다
            board[y][x] = False
            already_put.remove(x)
​
​
N = int(input())
​
# 체스판 그리기
board = [[False for i in range(N)] for j in range(N)]
​
# 상, 좌상, 우상 세가지만 확인
dx = [0, -1, +1]
​
# 이미 놓여진 x 좌표를 확인해서 아예 확인조차 하지 않도록 해보자
already_put = set()
​
cnt = 0
​
put_queen(0)
​
print(cnt)
​