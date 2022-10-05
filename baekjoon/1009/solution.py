// [문제 링크]: https://www.acmicpc.net/problem/1009

import sys
input = sys.stdin.readline
​
T = int(input())
​
for tc in range(T):
    a, b = map(int, input().split())
​
    if not a % 10:
        print(10)
        continue
​
    computer = 1
    while b:
        computer = (computer * a) % 10
        b -= 1
​
    print(computer)