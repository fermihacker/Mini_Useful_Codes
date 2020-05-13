import time,math

def check_Prime(n):
     if n<=1:
         return False
     md=math.floor(math.sqrt(n))
     for i in range(2,md+1):
         if(n%i==0):
             return False
     return True

def count():
     n=int(input("Enter the upper limit:"))
     s=time.time()
     k=0
     for i in range(1,n+1):
         if(check_Prime(i)==True):
             k+=1
     e=time.time()
     print("Total number of primes from 2 to",n,":",k)
     print("Time taken:",e-s)
count()
