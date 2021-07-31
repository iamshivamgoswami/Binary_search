class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        def func(l, x):

            n = len(l)
            if n == 0:
                return None
            lo = 0
            hi = n - 1
            res = 0
            while lo <= hi:
                mid = (lo + hi) // 2
                if l[mid] > x:
                    res = mid
                    hi = mid - 1
                else:
                    lo = mid + 1

            return l[res]
        return func(letters,target)