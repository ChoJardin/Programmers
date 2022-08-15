// [문제 링크]: https://leetcode.com/problems/roman-to-integer/submissions/

class Solution:
    def romanToInt(self, s: str) -> int:

        num_set = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9,
                   'X': 10, 'XL': 40, 'L': 50, 'XC': 90,
                   'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}

        temp = ''
        sum = 0

        while len(s) > 1:

            temp += s[0]
            s = s[1:]

            if temp+s[0] in num_set:
                temp += s[0]
                s = s[1:]

            sum += num_set[temp]
            temp = ''

        if s: sum += num_set[s]

        return sum