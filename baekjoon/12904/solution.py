// [문제 링크]: https://www.acmicpc.net/problem/12904

​
S = input()
T = input()
​
reachable = 0
​
while T:
​
    if T == S:
        reachable = 1
        break
​
    if len(T) == len(S):
        break
​
    if T.endswith('A'):
        T = T[:-1]
    elif T.endswith('B'):
        T = T[:-1]
        T = T[::-1]
​
print(reachable)
​
​
​
​