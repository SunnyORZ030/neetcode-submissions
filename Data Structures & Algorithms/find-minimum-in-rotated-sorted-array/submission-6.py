class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        ans = nums[right]

        while left < right:
            mid = (left + right) // 2

            if ans < nums[mid]:
                left = mid + 1
            else:
                ans = nums[mid]
                right = mid

        return ans