def knapsack(W,P,w,n):
    for i in range (1,n+1):
        for j in range (1,w+1):
            if W[i-1]<=j:
                kp[i][j]=max(kp[i-1][j],P[i-1]+kp[i-1][j-W[i-1]])
            else:
                kp[i][j]=kp[i-1][j]
    print(kp)

w=8
n=4
kp=[[0 for i in range(w+1)] for j in range (n+1)]
W=[3,4,5,6]
P=[2,3,4,1]

knapsack(W,P,w,n)
