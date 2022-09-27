// [문제 링크]: https://www.acmicpc.net/problem/2512

N = int(input())
requested = list(map(int, input().split()))
total = int(input())
​
# 오름차순으로 정렬
requested.sort()
​
# 모두 다 줄 수 있다면,
if sum(requested) <= total:
    print(max(requested))
​
# 모두 줄 수 없다면 계산이 필요함
else:
    for i in range(N):
​
        maxi = total // (N - i)
​
        if maxi <= requested[i]:
            print(maxi)
            break
​
        else:
            total -= requested[i]
​
​