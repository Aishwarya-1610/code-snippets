c=[1,5,7]
S=11
dp=[]

for i in range (S+1):
    dp.append(float('inf'))
dp[0]=0

for i in range(1,S+1):
    for j in range(len(c)):
        if(i-c[j]>=0):
            dp[i]=min(dp[i],dp[i-c[j]]+1)
            
print(dp)
