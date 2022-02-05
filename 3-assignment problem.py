def assign(cost,N):
  p=2**N
  dp=[]
  for i in range(p):
    dp.append(float('inf'))
    
  dp[0]=0
  for mask in range(p):
    y=bin(mask).replace("0b", "")
    s=''
    for i in range (N-len(y)):
      s+='0'
    y=s+y
    x=y.count('1')
    for j in range(N):
      if y[-(j+1)]!='1':
        dp[mask | (1<<j)]=min(dp[mask]+cost[x][j], dp[mask | (1<<j)])
  print(dp[p-1])
  print(dp)

N=3
cost=[[3, 2 ,7],[5, 1 ,3], [2, 7 ,2]]

minimum=assign(cost,N)
minimum
 
