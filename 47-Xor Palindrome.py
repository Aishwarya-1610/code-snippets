"""
A (1-indexed) binary string S of length N is called a xor palindrome if the value of Si⊕S(N+1−i) is the same for all 1≤i≤N.

For example, 0, 1111 and 0101 are xor palindromes, while 1110 and 110101 are not.

You are given a binary string S of length N. Determine if it is possible to rearrange it to form a xor palindrome or not.
"""
n = int(input())
for i in range (n):
    N=int(input())
    x=input()
    if(N%2==0):
        zeros=x.count('0')
        ones=x.count('1')
        if(zeros%2==0 and ones%2==0):
          print("YES")
        elif(zeros==ones):
          print("YES")
        else:
          print("NO")
    else:
        print("YES")
    
    
