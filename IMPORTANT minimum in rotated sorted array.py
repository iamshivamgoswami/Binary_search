class Solution:
    def findMin(self, l: List[int]) -> int:
        def solve(l):

            lo = 0
            n = len(l)
            if n == 1:
                return l[0]
            hi = n - 1
            while hi >= lo:
                # if the last element is greater than the first element then there is no rotation.
                # e.g. 1 < 2 < 3 < 4 < 5 < 7. Already sorted array.
                # Hence the smallest element is first element. A[0]
                # or return l[0] at end which will make it slightly slow
                if l[0] < l[hi]:
                    return l[0]
                mid = (lo + hi) // 2
                if l[(mid + 1) % n] >= l[mid] and l[((mid + n - 1) % n)] >= l[mid]:
                    return l[mid]
                elif l[mid] >= l[0]:
                    lo = mid + 1
                else:
                    hi = mid - 1

        return(solve(l))

