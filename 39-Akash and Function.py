"""
Akash has his maths test tomorrow. He secretly found out one of the questions from the test. As the test is online, he wants to write a code that solves the question. However, he is not good at coding and thus, wants Chef to help him with that.

Chef is given a function F(X) such that the condition:

F(X)=F(2⋅X)
holds true for all X, where X is a positive integer.
For a given positive integer N, find the maximum number of distinct elements in the array [F(1),F(2),F(3),…,F(N)].
"""
n = int(input())
for i in range (n):
    N=int(input())
    if(N%2==0):
        print(int(N/2))
    else:
       print(int((N+1)/2))
