import time
def pall():
     n=int(input("Enter a number to check:"))
     s=time.time()
     if(str(n)==str(n)[::-1]):
         print("Is Pallindrome")
     else:
         print("Is not Pallindrome")
     e=time.time()
     print("Time Taken=",e-s)

pall()

#Better:
isPall = lambda n : str(n) == str(n)[::-1]
