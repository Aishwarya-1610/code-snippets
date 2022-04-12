"""
You are given a binary string S and an integer K. In one operation, you can pick any bit and flip it, i.e turn 0 to 1 or 1 to 0. Can you make the string S a palindrome using exactly K operations?

Print YES if this is possible, and NO if it is not.
"""
n = int(input())
for i in range (n):
    x=input().split(' ')
    N=int(x[0])
    K=int(x[1])
    y=list(input())
    y=list(map(int,y))
    count=0
    for i in range(int(N/2)):
        #print(i)
        if(y[i]!=y[(N-1)-i]):
            count+=1
    if(K>=count and N%2==0 and (K-count)%2==0):
           print("YES")
    elif(K>=count and N%2!=0):
           print("YES")
    else:
           print("NO")
  
    
