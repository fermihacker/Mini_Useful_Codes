# This Is a file of the class containing all the methods on the main repo...


from math import sqrt,floor
from itertools import islice, count
from functools import reduce
class Methods:
    
    def __init__(self):
        pass


    def TranslateBinary(self, Code):        
        res = ''
        stuff = [Code[i:i+8] for i in range(0,len(Code),8)]
        for i in stuff:
            res += chr(int(eval('0b'+i)))
        return res
    
    def bubbleSort(self, array):
        tempLis = array
        for i in range(len(tempLis) - 1):
            for j in range(len(tempLis) - 1):
                if tempLis[j] > tempLis [j+1]:
                    tempLis[j], tempLis[j+1] = tempLis[j+1], tempLis[j]
        return tempLis
    
    def isPrime(self, number):
        if number == 0 or number == 1:
            return None
        if number == 2:
            return True
        return all([not(number % i == 0) for i in islice(count(2),floor(sqrt(number)))])
    
    
    def DigitalRoot(self, number):
        try:
            return eval('+'.join(list(str(number))))
        
        except:
            raise NotImplementedError
        
    def factors(self, number):    
        return set(reduce(list.__add__, 
                ([i, number//i] for i in range(1, int(number**0.5) + 1) if number % i == 0)))
    
    
    def InsertionSort(self, array):
        for i in range(1, len(array)):
            key = array[i]
            j = i - 1
            while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key 
        return array
    
    
    isPall = lambda self, element : str(element) == str(element)[::-1]
    
    def PrimeSieve(self, upperLimit):
        k = list(range(2,upperLimit))
        for i in k:
            j = 2
            while j < k[::-1][0]:
                if i*j in k:
                    k.remove(i*j)
                j += 1
        return k    
    
    def QuickSort(self,array):
        if len(array) <= 1:
            return array
        else:
            begin = QuickSort([i for i in array[1:] if i<array[0]])
            pivot = [array[0]]
            end = QuickSort([i for i in array[1:] if i >= array[0]])
            return begin + pivot + end
     
     
