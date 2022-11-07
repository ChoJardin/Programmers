// [문제 링크]: https://leetcode.com/problems/non-overlapping-intervals/submissions/

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        le, count= -9999999999, 0
        for start, end in sorted(intervals, key=lambda x: x[1]):
            if le > start: 
                count += 1 
            else: 
                le = end
        
        return count