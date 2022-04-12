"""
A binary string is called alternating if no two adjacent characters of the string are equal. Formally, a binary string T of length M is called alternating if Ti≠Ti+1 for each 1≤i<M.

For example, 0, 1, 01, 10, 101, 010, 1010 are alternating strings while 11, 001, 1110 are not.

You are given a binary string S of length N. You would like to rearrange the characters of S such that the length of the longest alternating substring of S is maximum. Find this maximum value.

A binary string is a string that consists of characters 0 and 1. A string a is a substring of a string b if a can be obtained from b by deletion of several (possibly, zero or all) characters from the beginning and several (possibly, zero or all) characters from the end.
"""
n = int(input())
for i in range (n):
    N=int(input())
    S=list(input())
    #print(S)
    z=S.count('0')
    o=S.count('1')
    #print(z)
    if z==o:
        print(z*2)
    elif z<o:
        print((2*z)+1)
    else:
        print((2*o)+1)
    
    
    
