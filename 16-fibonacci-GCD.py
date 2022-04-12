import math
import os
import random
import re
import sys


dp=[]
a=[]

N= 2 * 10^5
for i in range(N):
    dp.append(-1)

y=int(input())
for i in range(y):
    a.append(int(input()))
    
def fibonacci(n):
   if n==0:
      return 0
   if n==1:
      return 1
   if dp[n]!=-1:
      return dp[n]
   
   dp[n]=fibonacci(n-1)+fibonacci(n-2)
   return(dp[n])
  
def gcd(a, b):
    if(b == 0):
        return a
    else:
        return gcd(b, a % b)

    

n=a[0]
for i in range(1,len(a)):
     n=gcd(n,a[i])


dp[0]=0
dp[1]=1
print(fibonacci(n))


    
