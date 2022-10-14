// [문제 링크]: https://www.acmicpc.net/problem/1107

def perm():
    pass
​
​
def press(N, pressable):
​
    if not pressable:
        return abs(100 - int(N))
​
    possible = []
​
    made = ''
​
    need_press = list(N)
    for each in need_press:
        if each not in pressable:
            break
        made += each
    # 모든 버튼을 누를 수 있음
    else:
        return min(len(N), abs(100 - int(N)))
​
    # 한 자리 수 더 작은 제일 큰 수
    small = ''.join([max(pressable) for _ in range(len(N)-1)])
    possible.append(small)
​
    # 한 자리 수 더 큰 제일 작은 수
    if pressable[0] == '0':
        if len(pressable) == 1:
            big = [pressable[0]]
        else:
            big = [pressable[1]]
    else:
        big = [pressable[0]]
​
    big += [min(pressable) for _ in range(len(N))]
    possible.append(''.join(big))
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
            possible.append(unique_small)
            found = True
​
        if all(elem in pressable for elem in set(unique_big)):
            possible.append(unique_big)
            found = True
​
        step += 1
​
    diff = abs(int(N) - 100)
    for channel in possible:
        if not channel:
            channel = min(pressable)
​
        cur_diff = len(channel) + abs(int(channel) - int(N))
​
        if cur_diff < diff:
            diff = cur_diff
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