N=15
values=[2,3,7,8,10]
arr=[]
for i in range(N+1):
   arr.append(0)


for i in range (2,N+1):
  for j in range (1,int(i/2+1)):
    arr[i]= max(arr[i],values[j]+arr[i-(j+1)]


print(arr)
