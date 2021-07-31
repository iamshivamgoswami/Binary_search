import random
import time

a=[9,8,7,6,5,4,3,2,1]
k=1
start=0
end=len(a)-1
t=time.time()
while start<=end:
    mid=(start+end)//2
    if k==a[mid]:
        print(mid)
        break
    elif k>a[mid]:
        end=mid-1
    else:
        start=mid+1

else:
    print(-1)

print(time.time()-t)