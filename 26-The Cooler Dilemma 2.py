"""
The summer is at its peak in Chefland. Chef is planning to purchase a water cooler to keep his room cool. He has two options available:

Rent a cooler at the cost of X coins per month.
Purchase a cooler for Y coins.
Chef wonders what is the maximum number of months for which he can rent the cooler such that the cost of renting is strictly less than the cost of purchasing it.
"""
n = int(input())
for i in range (n):
    x=input().split(' ')
    x=list(map(int,x))
    if (x[1]==x[0] or (x[1]/x[0] < 1)):
        print(0)
    elif(x[1]%x[0]==0):
       print(int(x[1]/x[0])-1)
    else:
        print(x[1]//x[0])
    
