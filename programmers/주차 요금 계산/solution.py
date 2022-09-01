// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/92341

def solution(fees, records):

    def calcul_time(times):
        if len(times) % 2:
            times.append('23:59')

        minutes = 0
        for i in range(0, len(times), 2):
            in_h, in_m = map(int, times[i].split(':'))
            out_h, out_m = map(int, times[i+1].split(':'))

            # 분으로 계산
            if out_m < in_m:
                minutes += 60 - in_m + out_m
                minutes += 60 * (out_h - 1 - in_h)
            else:
                minutes += out_m - in_m
                minutes += 60 * (out_h - in_h)

        return minutes

    def calcul_fee(minutes):
        # 기본시간, 기본요금, 단위시간, 단위요금
        base_time, base_fee, part_time, part_fee = fees

        minutes_left = minutes
        fee = 0

        if minutes == 0:
            return fee

        if minutes > base_time:
            fee += base_fee
            minutes_left -= base_time

            while minutes_left > 0:
                fee += part_fee
                minutes_left -= part_time

            return fee

        return base_fee

    # 주차 기록 정리
    cars = dict()

    for record in records:
        time, number, condition = record.split(' ')

        if not cars.get(number):
            cars[number] = [time]
        else:
            cars[number].append(time)

    ans = []
    for car in sorted(cars.keys()):
        acc_time = calcul_time(cars[car])
        ans.append(calcul_fee(acc_time))

    return ans


