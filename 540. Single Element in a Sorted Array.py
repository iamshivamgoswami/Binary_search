class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) - 1

        while lo < hi:
            mid = (lo + hi) // 2
            even = (hi - mid) % 2 == 0
            if nums[mid + 1] == nums[mid]:
                if even:
                    lo = mid + 2
                else:
                    hi = mid - 1
            elif nums[mid - 1] == nums[mid]:
                if even:
                    hi = mid - 2
                else:
                    lo = mid + 1
            else:
                return (nums[mid])
        return nums[lo]


