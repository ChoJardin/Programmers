// [문제 링크]: https://www.acmicpc.net/problem/9461

T = int(input())
​
tc = [int(input()) for _ in range(T)]
​
triangles = [1, 1, 1, 2, 2]
​
for i in range(5, max(tc)):
    triangles.append(triangles[i-1] + triangles[i-5])
​
for each in tc:
    print(triangles[each-1])
​