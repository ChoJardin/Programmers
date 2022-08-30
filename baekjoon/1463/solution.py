// [문제 링크]: https://www.acmicpc.net/problem/1463

# 2의 배수라면? 2로 나눔/ -1
# 3의 배수라면? 3으로 나눔/ -1
# 6의 배수라면? 6으로 나눔/ -1
# 아무것도 아니면? -1
​
N = int(input())
​
memo = [0, 0, 1, 1]
​
for i in range(4, N+1):
    # 6의 배수
    if i % 6 == 0:
        memo.append(min(memo[i//3], memo[i//2], memo[i-1]) + 1)
​
    # 3의 배수
    elif i % 3 == 0:
        memo.append(min(memo[i//3], memo[i-1]) + 1)
​
    # 2의 배수
    elif i % 2 == 0:
        memo.append(min(memo[i//2], memo[i-1]) + 1)
​
    # 아무것도 아님
    else:
        memo.append(min(memo[i-1]+1, memo[i-2]+2))
​
print(memo[N])
​
​