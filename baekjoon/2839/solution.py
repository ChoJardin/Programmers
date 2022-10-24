// [문제 링크]: https://www.acmicpc.net/problem/2839

def dp(N):
​
    sugar = [-1, -1, -1, 1, -1, 1]
​
    if N < 6:
        return sugar[N]
​
    kilo = 6
    while kilo < N+1:
        possible = []
​
        if sugar[kilo-3] != -1:
            possible.append(sugar[kilo-3]+1)
​
        if sugar[kilo-5] != -1:
            possible.append(sugar[kilo-5]+1)
​
        if not possible:
            sugar.append(-1)
        else:
            sugar.append(min(possible))
​
        kilo += 1
​
    return sugar[-1]
​
​
print(dp(int(input())))