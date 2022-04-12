"""
Given a positive integer N, MoEngage wants you to determine if it is possible to rearrange the digits of N (in decimal representation) and obtain a multiple of 5.

For example, when N=108, we can rearrange its digits to construct 180=36⋅5 which is a multiple of 5.
"""



n = int(input())
for i in range (n):
    D=int(input())
    N=input()
    if ('0' in N) or ('5' in N):
        print('YES')
    else:
        print('NO')
