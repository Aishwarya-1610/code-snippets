"""
Dazzler has a task for you.

Given two positive integers A and B, find two positive integers i and j such that:

gcd(i,j)>1;
A≤i<j≤B;
The value (i+j) is minimum possible.
If there are multiple solutions, you may print any of them. If no such pair exists, print −1."""
n = int(input())
for i in range (n):
    x=input().split(' ')
    a=int(x[0])
    b=int(x[1])
    if a % 2==0:
        if b-a>=2:
           print(a,a+2)
        else:
            print("-1")
    else:
        if b-a>=3:
            if a%3==0:
                print(a,a+3)
            else:
                print(a+1,a+3)
        else:
            print(-1)

    
    
    
    
