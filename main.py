class Solution:
    ##Complete this function
    def searchInSorted(self,arr, n, x):
        left=0
        right=n-1
        while left<=right:
            mid=(left+right)//2

            if arr[mid]==x:
                return mid
            elif arr[mid]>x:
                left=mid+1
            else:
                right=mid-1

        return -1
a=Solution()
print(a.searchInSorted([1,2,3,4,6][::-1],5,4))