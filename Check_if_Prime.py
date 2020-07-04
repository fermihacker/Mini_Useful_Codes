from itertools import islice,count
from math import floor,sqrt

def prime(n):
    if n == 0 or n == 1:
        return None
    if n == 2:
        return True
    return all([not(n % i == 0) for i in islice(count(2),floor(sqrt(n)))])

