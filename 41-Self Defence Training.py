"""
After the phenomenal success of the 36th Chamber of Shaolin, San Te has decided to start 37th Chamber of Shaolin. The aim this time is to equip women with shaolin self-defence techniques.

The only condition for a woman to be eligible for the special training is that she must be between 10 and 60 years of age, inclusive of both 10 and 60.

Given the ages of N women in his village, please help San Te find out how many of them are eligible for the special training.

"""
n = int(input())
for i in range (n):
    N=int(input())
    x=input().split(' ')
    x=list(map(int,x))
    c=0
    for i in range (N):
        if x[i]>=10 and x[i]<=60:
            c=c+1
    print(c)
