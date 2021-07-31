
import heapq


def solve():


    d={}
    for  i in arr:
        if i-1 not in d:
            if i not in d:
                d[i]=[1]
            else:
                heapq.heappush(d[i],1)
        else:
            l=heapq.heappop(d[i-1])+1
            if len(d[i-1])==0:
                del d[i-1]
            if i not in d:
                d[i]=[]
            heapq.heappush(d[i],l)

    for v,arr in d.items():
        if len(arr)>0 and min(arr)<3:
            return False
    return True
