class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
         rows, cols = (numRows, numRows)
         a = [[0 for i in range(cols)] for j in range(rows)]
         arr=[]
         for i in range (numRows):
            for j in range (i+1):
                if (j==0 or j==i):
                    a[i][j]=1
                else:
                    a[i][j]=a[i-1][j]+a[i-1][j-1] 
         
         j=0
         for i in range (numRows):
                          
                arr.append(a[i][0:j+1])
                j=j+1
         return arr
