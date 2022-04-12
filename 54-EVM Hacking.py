"""
There are three cities and thus three EVMs. An insider told Chef that his party got A,B,C votes respectively in these three cities according to the EVMs. Also, the total number of votes cast are P,Q,R respectively for the three cities.

Chef, being the party leader, can hack at most one EVM so that his party wins. On hacking a particular EVM all the votes cast in that EVM are counted in favor of Chef's party.

A party must secure strictly more than half of the total number of votes cast in order to be considered the winner. Can Chef achieve his objective of winning by hacking at most one EVM?
"""
n = int(input())

for i in range (n):
    arr=[]
    x=input().split(' ')
    x=list(map(int,x))
    yy=x[0:3]
    xx=x[3:6]
    diff=0
    sum_xx=0
    sum_yy=0    
    for i in range(3):
      sum_yy+=yy[i]
      sum_xx+=xx[i]
      diff=max(diff,xx[i]-yy[i])
    if (float(sum_yy+diff)>float(sum_xx/2)):
         print("YES")
    else:
      print("NO")
    
    
