dp=[]
N=100
for i in range(N):
    dp.append(-1)

def fibonacci(n):
   if n==0:
      return 0
   if n==1:
      return 1
   if dp[n]!=-1:
      print(dp[n])
      return dp[n]
   
   dp[n]=fibonacci(n-1)+fibonacci(n-2)
   return(dp[n])
   
print(fibonacci(50))
