t=int(input())
for i in range(t):
    n=int(input())
    digit=list(str(n))
    if sum(list(map(int,digit)))%2==0:
        while(sum(list(map(int,digit)))%2==0):
            n=n+1
            digit=list(str(n))
        print(n)
    else:
        while(sum(list(map(int,digit)))%2!=0):
            n=n+1
            digit=list(str(n))
        print(n)
