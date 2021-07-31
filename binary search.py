class Solution:
    ##Complete this function
    def searchInSorted(self, arr, N, K):
        # Your code here
        l = 0
        r = N - 1
        while l <= r:
            mid = (r + l) // 2
            if K == arr[mid]:
                return 1
            elif K < arr[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return -1
