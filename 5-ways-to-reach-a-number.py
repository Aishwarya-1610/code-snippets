N=15
arr=[]
for i in range(N+1):
   arr.append(0)

arr[0]=1

for i in range (3,N+1):
    arr[i]+=arr[i-3]

for i in range (5,N+1):
    arr[i]+=arr[i-5]

for i in range (10,N+1):
    arr[i]+=arr[i-10]

print(arr[N])
