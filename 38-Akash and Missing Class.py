"""
Akash loves going to school, but not on weekends.

A week consists of 7 days (Monday to Sunday). Akash takes a leave every Saturday.

If a month consists of N days and the first-day of the month is Monday, find the number of days Akash would take a leave in the whole month.
"""
n = int(input())
for i in range (n):
    N=int(input())
    y=N%7
    x=N//7
    if (y==6):
        res=x+1
    else:
        res=x
    print(res)
