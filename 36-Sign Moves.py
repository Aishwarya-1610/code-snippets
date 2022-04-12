"""
Initially, Chef is at coordinate 0 on X-axis. For each i=1,2,…,N in order, Chef does the following:

If Chef is at a non-negative coordinate, he moves i steps backward (i.e, his position's coordinate decreases by i), otherwise he moves i steps forward (i.e, his position's coordinate increases by i).
You are given the integer N. Find the final position of Chef on the X-axis after N operations.
"""
n = int(input())
for i in range (n):
    N=int(input())
    if N%2==0:
        print(N//2)
    else:
        print(-1*(N+1)//2)
    
