# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, x: int, MountainArray: 'MountainArray') -> int:
        def func():

            lo = 0
            n = MountainArray.length()
            hi = n - 1
            while lo < hi:
                mid = (lo + hi) // 2
                a = MountainArray.get(mid)
                b = MountainArray.get(mid + 1)
                if a < b:
                    lo = mid + 1
                else:
                    hi = mid

            return lo

        index = func()

        def bs(lo, hi, x):
            while lo <= hi:
                mid = (lo + hi) // 2
                a = MountainArray.get(mid)
                if a == x:
                    return mid
                elif a > x:
                    hi = mid - 1
                else:
                    lo = mid + 1
            return -1

        def aabs(lo, hi, x):
            while lo <= hi:
                mid = (lo + hi) // 2
                a = MountainArray.get(mid)
                if a == x:
                    return mid
                elif a < x:
                    hi = mid - 1
                else:
                    lo = mid + 1
            return -1

        left = bs(0, index - 1, x)
        right = aabs(index, MountainArray.length() - 1, x)
        if left >= 0 and right >= 0:
            return min(left, right)

        if left < 0:
            return right
        if right < 0:
            return left







