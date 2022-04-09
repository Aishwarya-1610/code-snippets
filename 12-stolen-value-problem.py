values =[9,3,5,8,2,4,7]
n=len(values)
dp=[0 for i in range(n+1)]
dp[1]=values[0]
for i in range (2,n+1):
    dp[i]=max(dp[i-1],dp[i-2]+values[i-1])
print(dp[n])
