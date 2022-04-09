import math

def catalan(n,arr):
    for i in range (1,n+1):
         #print(i)
         fact=math.factorial(i)
         fact1=math.factorial(2*i)
         x=fact1/(fact*fact)
         y=1/(i+1)
         z=x*y
         arr.append(int(z))
         print(arr)
    return arr
 
arr=[1]    
arr=catalan(5,arr)
print(arr)
