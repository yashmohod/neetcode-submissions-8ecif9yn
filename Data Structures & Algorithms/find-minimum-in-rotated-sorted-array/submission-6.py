class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                # mid is in the left (higher) portion, min is to the right
                l = mid + 1
            else:
                # mid is in the right (lower) portion, min is at mid or to the left
                r = mid

        return nums[l]