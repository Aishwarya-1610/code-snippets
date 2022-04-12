"""
Chef recently realized that he needs a haircut, and went to his favorite hair salon. At the salon, he found N customers waiting for their haircuts. From his past experience, Chef knows that the salon takes M minutes per customer. Only one person can get their haircut at a time.

For how many minutes will Chef have to wait before he can get his haircut?
"""
n = int(input())
for i in range (n):
    x=input().split(' ')
    N=int(x[0])
    M=int(x[1])
    print(N*M)
