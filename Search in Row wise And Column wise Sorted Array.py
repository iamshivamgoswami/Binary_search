class Solution:
	def matSearch(self,arr, n, m, x):
		i=0
		j=m-1
		while i>=0 and i<n and j>=0 and j <m:
		    if arr[i][j]==x:
		        return 1
		    elif arr[i][j]>x:
		        j-=1
		    else:
		        i+=1
	    return 0
