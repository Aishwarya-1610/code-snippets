S=11
dp=[]


for i in range (S+1):
    dp.append(0)

for i in range(1,S+1):
    for j in range(1,i+1):
        if(j<=6):
            dp[i]=dp[i]+dp[i-j]
            
print(dp[S])
