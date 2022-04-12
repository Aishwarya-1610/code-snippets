"""
A particular month has 30 days, numbered from 1 to 30.

Day 1 is a Monday, and the usual 7-day week is followed (so day 2 is Tuesday, day 3 is Wednesday, and so on).

Every Saturday and Sunday is a holiday. There are N festival days, which are also holidays. Note that it is possible for a festival day to occur on a Saturday or Sunday.

You are given the dates of the festivals. Determine the total number of holidays in this month.
"""
n = int(input())
for i in range (n):
    N=int(input())
    x=input().split(' ')
    x=list(map(int,x))
    count=8
    for i in range (N):
        if (x[i]%7!= 6 and x[i]%7!=0):
            count=count+1
    print(count)
    
