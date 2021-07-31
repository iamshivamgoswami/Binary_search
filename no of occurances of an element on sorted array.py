class Solution:
    def count(self, arr, n, x):
        start = 0
        end = n - 1
        a = -1
        while start <= end:
            mid = (start + end) // 2
            if x == arr[mid]:
                a = mid
                end = mid - 1
            elif x < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        start = 0
        end = n - 1
        b = -1
        while start <= end:
            mid = (start + end) // 2
            if x == arr[mid]:
                b = mid
                start = mid + 1
            elif x < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return b - a + 1 if b!=-1 else 0