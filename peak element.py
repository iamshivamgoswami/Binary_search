class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def func(arr):
            if len(arr)==1:
                return 0
            lo = 0
            hi = len(arr) - 1
            n = len(arr)
            while lo <= hi:
                mid = (lo + hi) // 2
                if mid > 0 and mid < n - 1:
                    if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
                        return mid
                    elif arr[mid] < arr[mid + 1]:
                        lo = mid + 1
                    else:
                        hi = mid - 1
                elif mid == 0:
                    if arr[0] > arr[1]:
                        return 0
                    else:

                        return 1
                else:
                    if arr[n - 1] > arr[n - 2]:
                        return n - 1
                    else:
                        return n - 2

        return(func(nums))

