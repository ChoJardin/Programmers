// [문제 링크]: https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        return sorted(nums)[int(f'-{k}')]
        