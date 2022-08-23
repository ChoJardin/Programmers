// [문제 링크]: https://www.acmicpc.net/problem/1158

N, K = map(int, input().split())
​
ans = []
​
# 앉아있다
arr = [i for i in range(1, N+1)]
​
# 지울 idx
to_pop = 0
while arr:
    if to_pop + K-1 < len(arr):
        to_pop = to_pop + K -1
    else:
        to_pop = (to_pop + K-1) % len(arr)
​
    ans.append(arr.pop(to_pop))
    
to_string = ', '.join(list(map(str, ans)))
​
print(f'<{to_string}>')