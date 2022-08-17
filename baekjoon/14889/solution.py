// [문제 링크]: https://www.acmicpc.net/problem/14889

from itertools import combinations
​
N = int(input())
ability = [list(map(int, input().split())) for i in range(N)]
​
# 확인한 조합 들어가겠음
checked = set()
​
players = [i for i in range(N)]
teams = list(combinations(range(N), N//2))
​
min_difference = 999999999
​
for first_team in teams:
    if not checked.__contains__(first_team):
        # 일단 확인한 조합으로 넣어주기
        second_team = tuple(filter(lambda x: x not in first_team, players))
        checked.add(first_team)
        checked.add(second_team)
​
        # 각 팀 별 능력치 계산
        # S12와 S21이 다르기 때문에 2개짜리 순열로 뽑아서 능력치 값 불러온 다음에 합하기
        # 혹은 조합으로 해서 idx 01/ 10 으로도 가능
        first_ability = sum(map(lambda x: ability[x[0]][x[1]] + ability[x[1]][x[0]], list(combinations(first_team, 2))))
        second_ability = sum(map(lambda x: ability[x[0]][x[1]]+ ability[x[1]][x[0]], list(combinations(second_team, 2))))
​
        min_difference = min(min_difference, abs(first_ability-second_ability))
​
print(min_difference)