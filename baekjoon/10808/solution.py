// [문제 링크]: https://www.acmicpc.net/problem/10808

S = list(input())
​
cnt = [0 for _ in range(26)]
​
for each in S:
    cnt[ord(each) - 97] += 1
​
print(*cnt)