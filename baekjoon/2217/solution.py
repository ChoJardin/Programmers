// [문제 링크]: https://www.acmicpc.net/problem/2217

import sys, heapq
​
input = sys.stdin.readline
​
N = int(input())
​
queue = []
​
# 최소힙으로 만들겠음
for _ in range(N):
    heapq.heappush(queue, int(input()))
​
# 최대 무게
max_weight = -999999999
​
# 현재 heap 의 길이
current_len = len(queue)
​
# 하나씩 빼주면서 최댓값 찾을 것
for _ in range(N):
​
    # 현재 가능한 무게
    current_weight = queue[0] * current_len
​
    if current_weight > max_weight:
        max_weight = current_weight
​
    heapq.heappop(queue)
    current_len -= 1
​
print(max_weight)