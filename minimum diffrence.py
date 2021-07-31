def func():
    arr=[1,2,3,4,5,6,7,11,12]
    x=1
    lo=0
    hi=len(arr)-1
    res=0
    while lo<=hi:
        mid=(lo+hi)//2
        if arr[mid]==x:
            return abs(arr[mid]-x)
        elif arr[mid]>x:
            res=mid
            hi=mid-1
        else:
            lo=mid+1

    lo=0
    hi=len(arr)-1
    ans=-1
    while lo<=hi:
        mid=(lo+hi)//2
        if arr[mid]==x:
            return abs(arr[mid]-x)
        elif arr[mid]>x:

            hi=mid-1
        else:
            ans=mid
            lo=mid+1
    if x>arr[-1]:

        res=len(arr)-1
    if x<arr[0]:
        ans=0
    print(res,ans)
    return min(abs(x-arr[res]),abs(x-arr[ans]))


print(func())


