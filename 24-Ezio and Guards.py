"""
Ezio can manipulate at most X number of guards with the apple of eden.

Given that there are Y number of guards, predict if he can safely manipulate all of them.
"""
n = int(input())
for i in range (n):
    x=input().split(' ')
    x=list(map(int,x))
    if (x[0]>=x[1]):
        print("yes")
    else:
        print("no")
