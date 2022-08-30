// [문제 링크]: https://www.acmicpc.net/problem/1182

def get_sum(idx):
    global cnt
​
    if idx == N:
        sub_total = 0
​
        for i in range(N):
            if not picked.count(True):
                return
​
            if picked[i]:
                sub_total += nums[i]
​
        if sub_total == S:
            cnt += 1
​
        return
​
    picked[idx] = True
    get_sum(idx+1)
    picked[idx] = False
    get_sum(idx+1)
​
​
N, S = map(int, input().split())
​
nums = list(map(int, input().split()))
​
cnt = 0
​
picked = [False for _ in range(N)]
​
get_sum(0)
​
print(cnt)