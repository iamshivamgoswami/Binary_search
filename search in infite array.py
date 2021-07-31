import random
import time
arr=[random.randint(1,100000000)for i in range(10000000)]
arr.sort()

def func(arr):


    x=arr[500000]


    lo=0
    hi=1
    while arr[hi]<x:
        hi*=2
    print(hi)
    while lo<=hi:
        mid=(lo+hi)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            hi=mid-1
        else:
            lo=mid+1
start=time.time()
print(func(arr))
print(time.time()-start)
