"""
Chef invented a modified wordle.

There is a hidden word S and a guess word T, both of length 5.

Chef defines a string M to determine the correctness of the guess word. For the ith index:

If the guess at the ith index is correct, the ith character of M is G.
If the guess at the ith index is wrong, the ith character of M is B.
Given the hidden word S and guess T, determine string M.
"""
n = int(input())
for i in range (n):
    x=input()
    y=input()
    temp=''
    for i in range(len(x)):
        if (x[i]!=y[i]):
            temp=temp+'B'
        else:
            temp=temp+'G'
            
    print(temp)
    
