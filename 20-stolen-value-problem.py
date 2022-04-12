S=11
dp=[]


for i in range (S+1):
    dp.append(0)

for i in range(1,S+1):
    dp[i]=max(dp[i-1]+dp[i-2]+values[i])
            
print(dp[S])
