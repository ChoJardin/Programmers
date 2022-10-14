// [문제 링크]: https://www.acmicpc.net/problem/1107

def press(N, pressable):
​
    if not pressable:
        return abs(100 - int(N))
​
    possible = ''
​
    need_press = list(N)
    for each in need_press:
        if each not in pressable:
            break
    # 모든 버튼을 누를 수 있음
    else:
        return min(len(N), abs(100 - int(N)))
​
    # 같은 자리 수
    num_n = int(N)
    step = 1
    found = False
    while not found:
        unique_small = str(num_n - step)
        unique_big = str(num_n + step)
​
        if all(elem in pressable for elem in set(unique_small)):
            possible = unique_small
            found = True
            continue
​
        if all(elem in pressable for elem in set(unique_big)):
            possible = unique_big
            found = True
            continue
​
        step += 1
​
    diff = min(abs(int(N) - 100), len(possible) + abs(int(possible) - int(N)))
​
    return diff
​
​
N = input()
M = int(input())
broken = list(input().split()) if M else []
​
pressable = [str(i) for i in range(10) if str(i) not in broken]
​
print(press(N, pressable))