// [문제 링크]: https://leetcode.com/problems/majority-element/submissions/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        unique_nums = list(set(nums))
        
        majority = None 
        cnt = -1 
        
        for num in unique_nums: 
            if nums.count(num) > cnt: 
                majority = num 
                cnt = nums.count(num)
        
        return majority
        
        