class Solution:
    def findMin(self, nums: List[int]) -> int:
        def solve(l):

            lo = 0
            n = len(l)

            hi = n - 1
            while hi > lo:

                pivot = (lo + hi) // 2
                if l[pivot] < l[hi]:
                    hi = pivot
                elif l[pivot] > l[hi]:
                    lo = pivot + 1
                else:
                    hi -= 1
            return l[lo]

        return (solve(nums))
