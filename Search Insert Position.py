class Solution:
    def searchInsert(self, l: List[int],x: int) -> int:
        lo = 0
        hi = len(l) - 1
        res = -1

        while lo <= hi:
            mid = (lo + hi) // 2

            if l[mid] == x:

                return mid
            elif l[mid] < x:

                res = mid

                lo = mid + 1
            elif l[mid] > x:
                hi = mid - 1
        return res + 1

