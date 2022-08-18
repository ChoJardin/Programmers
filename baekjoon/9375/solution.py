// [문제 링크]: https://www.acmicpc.net/problem/9375

from functools import reduce
​
TC = int(input())
​
for test in range(TC):
​
    N = int(input())
​
    # 옷이 하나도 없음
    if not N:
        print(0)
        continue
​
    # 혜빈이가 가진 옷 정리
    closet = {}
    for _ in range(N):
        v, k = input().split()
​
        if closet.__contains__(k):
            closet[k].add(v)
            continue
​
        closet[k] = {v}
    
    # 조합의 개수 구하기 
    # 옷의 종류의 개수 +1 의 곱 -1 
    print(reduce(lambda acc, cur: acc * (len(cur) + 1), list(closet.values()), 1) - 1)