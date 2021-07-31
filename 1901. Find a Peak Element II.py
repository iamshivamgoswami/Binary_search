def func():

    lo=0
    n=len(arr)
    hi=len(arr[0])-1
    while lo<=hi:
        maxx=0
        mid=(lo+hi)//2
        for i in range(n):
            maxx=i if (arr[i][mid]>=arr[maxx][mid]) else maxx
        left=mid-1>=lo and arr[maxx][mid-1]>arr[maxx][mid]
        right=mid+1<=hi and arr[maxx][mid+1]>arr[maxx][mid]

        if not left and not right:
            return [maxx,mid]
        elif left:
            hi=mid-1
        else:
            lo=mid+1

print(func())