class Solution:


    def findPages(self, arr, n, m):
        def func(arr,k):

            lo = max(arr)
            hi = sum(arr)

            res = -1


            if len(arr) < k:
                return res
            while lo <= hi:

                mid = (lo + hi) // 2

                if isvalid(arr, k, mid):

                    res = mid
                    hi = mid - 1
                else:
                    lo = mid + 1

            return res

        def isvalid(arr, k, maxx):
            count = 1
            summ = 0
            for i in range(len(arr)):

                summ += arr[i]
                if summ > maxx:
                    count += 1
                    summ = arr[i]
            if count > k:
                return False
            return True

        return(func(arr,m))