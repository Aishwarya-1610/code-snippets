def editdistance(S,D,l1,l2):
    ED=[[0 for i in range (l2+1)] for j in range (l1+1)]
    for i in range(l1+1):
        ED[i][0]=i
    for j in range(l2+1):
        ED[0][j]=j
    for i in range(1,l1+1):
        for j in range(1,l2+1):
            if S[i-1]==D[j-1]:
                ED[i][j]=ED[i-1][j-1]
            else:
                ED[i][j]=1+min(ED[i-1][j-1],ED[i-1][j],ED[i][j-1])
            
    return ED[l1][l2]
    

s1='apiskal'
s2='vishal'

res=editdistance(s1,s2,len(s1),len(s2))
print(res)
