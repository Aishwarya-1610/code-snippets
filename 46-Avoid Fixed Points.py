"""
Chef has a sequence of N integers A=[A1,A2,…,AN]. He can perform the following operation any number of times (possibly, zero):

Choose any positive integer K and insert it at any position of the sequence (possibly the beginning or end of the sequence, or in between any two elements).
For example, if A=[5,3,4] and Chef selects K=2, then after the operation he can obtain one of the sequences [2–,5,3,4],[5,2–,3,4],[5,3,2–,4], or [5,3,4,2–].

Chef wants this sequence to satisfy the following condition: for each 1≤i≤∣A∣, Ai≠i. Here, ∣A∣ denotes the length of A.

Help Chef to find the minimum number of operations that he has to perform to achieve this goal. It can be proved that under the constraints of the problem, it's always possible to achieve this goal in a finite number of operations.
"""

n = int(input())
for i in range (n):
    c=0
    j=0
    N=int(input())
    x=input().split(' ')
    x=list(map(int,x))
    for k in range (N):
       if(x[k]-(k+1)==j):
          c+=1
          j+=1
    print(c)
    
