// [문제 링크]: https://www.acmicpc.net/problem/15565

N, K = map(int, input().split())
puppets = list(map(int, input().split()))
​
# ryan 위치만 저장
ryan = []
for i in range(N):
    if puppets[i] == 1:
        ryan.append(i)
​
# ryan 개수 부족
if len(ryan) < K:
    print(-1)
​
# ryan 개수 딱 맞음
elif len(ryan) == K:
    print(ryan[-1] - ryan[0] + 1)
​
# 최소 길이 찾아야 함
else:
    min_size = N
​
    for i in range(len(ryan) - K + 1):
​
        cur = ryan[i+K-1] - ryan[i] + 1
​
        if min_size > cur:
            min_size = cur
​
        else:
            continue
​
    print(min_size)