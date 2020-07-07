import re
from itertools import islice,count
from math import floor,sqrt
from functools import reduce


# This module consists of different methods that are useful

def messageFromBinaryCode(codedString):
    '''This Function enables you to convert a binary string to a character string'''
    decodedMessage = ''
    inputStringSplit = [codedString[i:i+8] for i in range(0,len(codedString),8)]
    for i in inputStringSplit:
        decodedMessage += chr(int(eval('0b'+i)))
    return decodedMessage

def bubbleSort(inputArray):
    '''This Method performs bubble sort on a given array and returns sorted array'''
    temporaryArray = inputArray
    for i in range(len(temporaryArray) - 1):
        for j in range(len(temporaryArray) - 1):
            if temporaryArray[j] > temporaryArray [j+1]:
                temporaryArray[j], temporaryArray[j+1] = temporaryArray[j+1], temporaryArray[j]
    return temporaryArray


def isPrime(inputNumber):
    '''Checks if a number is prime or not'''
    if inputNumber == 0 or inputNumber == 1:
        return None
    if inputNumber == 2:
        return True
    return all([not(inputNumber % i == 0) for i in islice(count(2),floor(sqrt(inputNumber)))])



def DigitalRoot(number):
    '''Calculates the digital root of a number, i.e. the sum of digits of a number'''
    try:
        return eval('+'.join(list(str(number))))
    except Exception as e:
        raise Exception
    # example: DigitalRoot(12345) = 1+2+3+4+5 = 15
    
def factors(number):    
    '''Returns the set of factors of a number'''
    return set(reduce(list.__add__,
                    ([i, number//i] for i in range(1, int(number**0.5) + 1) if number % i == 0)))


def emailParser(email):
    '''This program parses an email for username and domain'''    
    domain = re.findall(r'[\w+\.\w]+',email)[::-1][0]
    username = email[:email.find(domain) - 1]
    return 'Username: {}\nDomain: {}'.format(username,domain)
    
def isPallindrome(inputNumber):
    '''This returns a bool val checking if a number/string is a pallindrome or not'''
    return str(inputNumber) == str(inputNumber)[::-1]

def primeSieve(inputNumber):
    '''Returns a list of prime numbers less than inputNumber'''
    numberList = list(range(2,inputNumber))
    for i in numberList:
        j = 2
        while j < numberList[::-1][0]:
            if i*j in numberList:
                numberList.remove(i*j)
            j += 1
    return numberList


def QuickSort(inputArray):
    '''
    Taking the pivot as the first element of the array.
    This method applies quick sort on provided array and returns a sorted array
    '''
    if len(inputArray) <= 1:
        return inputArray
    else:
        begin = QuickSort([i for i in inputArray[1:] if i<inputArray[0]])
        pivot = [inputArray[0]]
        end = QuickSort([i for i in inputArray[1:] if i >= inputArray[0]])
        return begin + pivot + end

def SelectSort(inputArray):
    '''Applies select sort on the inputArray and returns the sorted array'''
    tempArray = inputArray
    sortedArray = []
    while len(tempArray) > 0:
        sortedArray.append(min(tempArray))
        tempArray.remove(min(tempArray))
    return sortedArray


def insertionSort(inputArray):
    '''Applies insertion sort on the inputArray and returns the sorted array'''
    for i in range(1, len(inputArray)):
        key = inputArray[i]
        j = i - 1
        while j >= 0 and key < inputArray[j]:
            inputArray[j + 1] = inputArray[j]
            j -= 1
        inputArray[j + 1] = key 
    return inputArray
