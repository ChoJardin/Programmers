// [문제 링크]: https://leetcode.com/problems/binary-search/submissions/

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binary(start, end):

            # 찾지 못한 경우
            if start > end:
                return -1

            mid = (start + end) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                return binary(start, mid-1)

            else:
                return binary(mid+1, end)

        return binary(0, len(nums)-1)