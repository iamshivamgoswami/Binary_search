def func():

    l=[1,3,5,6]
    x=2
    lo = 0
    hi = len(l) - 1
    res=-1

    while lo <= hi:
        mid = (lo + hi) // 2

        if l[mid]==x:

            return l[mid+1
        elif l[mid]<x:

            res=mid

            lo=mid+1
        elif l[mid]>x:
            hi=mid-1
    return res+1


print(func())
