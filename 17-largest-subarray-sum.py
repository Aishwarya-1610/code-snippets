def Kadane(arr):
    maximum=0
    tmax=0
    for i in range(n):
        tmax=tmax+arr[i]
        if tmax<0:
            tmax=0
        if maximum<tmax:
            maximum=tmax
    return maximum
    
arr=[1,-3,4,6,-6,-9,4,8]
res=Kadane(arr)
print(res)
