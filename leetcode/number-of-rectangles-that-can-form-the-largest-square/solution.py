// [문제 링크]: https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/submissions/

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        # 둘 중 더 짦은 길이만 남겨서, 그 중 max 인 길이가 몇개가 있는지 센다!
        square_lengths = list(map(lambda x: min(x), rectangles))
        
        square_lengths.sort(reverse=True) 
        
        max_length = square_lengths[0] 
        cnt = 0 
        
        for length in square_lengths: 
            if length == max_length: 
                cnt += 1 
            else: 
                break
                
        return cnt