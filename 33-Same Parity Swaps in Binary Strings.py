"""
You are given a binary string S of length N (i.e. every character of S is either 0 or 1).

You can perform the following operation on S:

select any two indices i,j of the same parity, i.e. either both i,j are odd or both i,j are even
swap Si and Sj
For example, in the string 1110, we can swap the second and the fourth characters to get 1011. However, we can never obtain 1101 from 1110 by performing such swaps.

Find the maximum possible number of occurrences of the string 01 as a substring of S after performing the above operation any number of times (it is also allowed to not perform any operation).

For example, the string 1110 has no occurrence of the string 01 as a substring, whereas we can swap the second and fourth characters to obtain 1011 which has exactly one occurrence of 01 (colored red).
"""
t = int(input())
for i in range (t):
    n = int(input())
    s = input()
    m = s.count('01')
    arr = list(s.split())
    check = True
    t0 = 0 
    t1 = 0
    if n%2==0:
        for i in range(0,n-1,2):
            if s[i]!='0' or s[i+1]!='1':
                check = False
                break
        if check:
            print(n//2)
            continue
    for i in s:
        if i=='0':
            t0 +=1 
        else:
            t1 +=1
    if t0==t1:
        print(t1-1)
        continue
    print(min(t0,t1))
                
            
            
    
