// [문제 링크]: https://leetcode.com/problems/container-with-most-water/submissions/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        max_water = -99999
        
        left = 0
        right = len(height)-1
        
        width = right
        
        while left < right: 
            cur_water = width * min(height[left], height[right])
            
            if cur_water > max_water: 
                max_water = cur_water 
            
            if height[left] < height[right]: 
                left += 1 
            else: 
                right -= 1
            
            width -= 1 
            
        return max_water