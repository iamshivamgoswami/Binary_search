class Solution:
    def search(self, arr: List[int], x: int) -> int:
        lo = 0
        hi = len(arr) - 1
        if arr[0] == x:
            return True

        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid] < arr[hi]:
                hi = mid

            elif arr[mid] > arr[hi]:
                lo = mid + 1
            else:
                hi -= 1
        ans = lo

        def bs(arr, lo, hi, x):
            #below line is important
            while lo <= hi and arr[lo] == arr[hi]:
                if arr[lo] == x:
                    print(1)
                    return True
                lo += 1
                hi -= 1

            while lo <= hi:
                mid = (lo + hi) // 2
                if arr[mid] == x:
                    return mid
                elif arr[mid] > x:
                    hi = mid - 1
                else:
                    lo = mid + 1

        res = (bs(arr, 0, ans - 1, x)) or (bs(arr, ans, len(arr) - 1, x))
        return True if res else False

