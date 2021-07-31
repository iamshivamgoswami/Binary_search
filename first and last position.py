class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lo = 0
        hi = len(nums) - 1
        res = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if target == nums[mid]:
                res = mid
                hi = mid - 1
            elif target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1

        b = -1
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if target == nums[mid]:
                b = mid

                lo = mid + 1
            elif target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1

        return [res, b]
