"""
Chef is planning to buy a new car for his birthday. After a long search, he is left with 2 choices:

Car 1: Runs on diesel with a fuel economy of x1 km/l
Car 2: Runs on petrol with a fuel economy of x2 km/l
Chef also knows that

the current price of diesel is y1 rupees per litre
the current price of petrol is y2 rupees per litre
Assuming that both cars cost the same and that the price of fuel remains constant, which car will minimize Chef's expenses?

Print your answer as a single integer in the following format

If it is better to choose Car 1, print −1
If both the cars will result in the same expenses, print 0
If it is better to choose Car 2, print 1
"""
n = int(input())
for i in range (n):
    x=input().split(' ')
    x=list(map(int,x))
    x1,x2,y1,y2=x
    car1=y1/x1
    car2=y2/x2
    if car1==car2:
     print("0")
    if car2>car1:
     print("-1")
    if car1>car2:
     print("1")
    
