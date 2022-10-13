// [문제 링크]: https://www.acmicpc.net/problem/1654

def find_length(N, cables):
​
    lack = max(cables)+1
    over = 1
    checked = set()
​
    checked.add(lack)
    checked.add(over)
​
    while (lack+over) // 2 not in checked:
        mid = (lack+over) // 2
​
        cap_cable = 0
        for cable in cables:
            cap_cable += cable // mid
​
        if cap_cable < N and lack > mid:
            lack = mid
            checked.add(mid)
​
        elif cap_cable >= N and over < mid:
            over = mid
            checked.add(mid)
​
    return over
​
​
K, N = map(int, input().split())
​
cables = [int(input()) for _ in range(K)]
​
print(find_length(N, cables))
​
​
​