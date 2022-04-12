"""
Chef attempted an exam consisting of N objective questions. The marking scheme of the exam is:

+3 marks for a correct answer.
−1 marks for an incorrect answer.
0 marks for an unattempted question.
Find whether it is possible for Chef to score exactly X marks.

If it is possible, print 3 integers A, B, and C denoting the number of correct answers, incorrect answers and unattempted questions respectively.
"""
n = int(input())
for i in range (n):
    x=input().split(' ')
    N=int(x[0])
    X=int(x[1])
    a=0
    b=0
    c=0
    if (X%3==0):
      a=X/3
    elif(X%3==1):
      a=int(X/3)+1 
      b=2
    elif(X%3==2):
      a=int(X/3)+1
      b=1
    
    if ((a+b)<=N):
        print("YES")
        print(int(a),end=" ")
        print(int(b),end=" ")
        print(int(N-(a+b)))
    else:
        print("NO")
