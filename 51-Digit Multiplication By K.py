"""
There is a strange game played in ChefLand.

The game starts with N white balls, the i-th of which has a power of Si. It is known that 0≤Si≤9. On each level, a black ball with power K hits each of the white balls. After the collision, the power of each white ball is multiplied by K.

However, white balls are only allowed to have single-digit power. In order to maintain this, a white ball whose power contains multiple digits splits into several white balls with single-digit power, one per digit.

For example, consider a white ball with a power of 4.

If K=2, its resulting power is 8 and it remains a single ball.
If K=13, its resulting power is 52, so it splits into two white balls with power 5 and 2 respectively.
If K=27, its resulting power is 108, so it splits into three white balls with power 1, 0, and 8 respectively.
The aim of the game is to determine the number of white balls after M levels. Note that K remains the same for every level.

Please help Chef win the game. Since the answer can be large, print it modulo 109+7.
"""

n = int(input())
for i in range (n):
    x=input().split(' ')
    N=int(x[0])
    K=int(x[1])
    M=int(x[2])
    S=list(input())
    #S=list(map(int,S))
    if(S=='0'):
        print('1')
        continue
    for i in range(M):
       s=''
       for i in range(len(S)):
          element=int(S[i])
          S[i]=element * K
          s+=str(S[i])
       S=list(s)
       
    print(len(S))
    
