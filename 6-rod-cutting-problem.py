N=15
arr=[]
for i in range(N+1):
   arr.append(0)


for i in range (2,N+1):
  for j in range (1,int(i/2+1)):
    arr[i]= max(arr[i],max((j*(i-j),(j*arr[i-j]))))


print(arr)
