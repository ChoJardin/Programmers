// [문제 링크]: https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/submissions/

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        # 둘 중 더 짦은 길이만 남겨서, 그 중 max 인 길이가 몇개가 있는지 센다!
        square_lengths = list(map(lambda x: min(x), rectangles))

        length_cnt = dict()

        for length in square_lengths:
            length_cnt[length] = length_cnt.get(length, 0) + 1

        return length_cnt[max(length_cnt.keys())]