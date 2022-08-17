// [문제 링크]: https://www.acmicpc.net/problem/14889

from itertools import combinations, permutations
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
        first_ability = sum(map(lambda x: ability[x[0]][x[1]], list(permutations(first_team, 2))))
        second_ability = sum(map(lambda x: ability[x[0]][x[1]], list(permutations(second_team, 2))))
​
        min_difference = min(min_difference, abs(first_ability-second_ability))
​
print(min_difference)