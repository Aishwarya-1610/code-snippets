 
def longestcommonsubsequence(s1,s2):
    len_s1=len(s1)
    len_s2=len(s2)
    rows, cols = (len_s1+1,len_s2+1)
    LCS = [[0 for i in range(cols)] for j in range(rows)]
    for i in range (1,len_s1+1):
        #print(i)
        for j in range (1,len_s2+1):
            if (s1[i-1]==s2[j-1]):
                LCS[i][j]=LCS[i-1][j-1]+1
            else:
                LCS[i][j]=max(LCS[i-1][j],LCS[i][j-1])
    return LCS[len_s1][len_s2]
    
s1='abcda'
s2=s1[-1]
res=longestcommonsubsequence(s1,s2)
print(len(s1)-res)
