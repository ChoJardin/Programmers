// [문제 링크]: https://leetcode.com/problems/intersection-of-two-arrays/submissions/

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # 1. set 으로 중복 제거 
        # 2. 둘 중 길이가 더 짧은 애를 기준으로 검색 
        
        unique_nums1 = set(nums1)
        unique_nums2 = set(nums2)
        
        if len(unique_nums1) > len(unique_nums2): 
            base = unique_nums2
            compare = unique_nums1 
        else: 
            base = unique_nums1
            compare = unique_nums2
            
        intersection = [] 
        
        for each in base: 
            if each in compare: 
                intersection.append(each)
        
        return intersection