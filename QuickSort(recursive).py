
#Taking the pivot as the first element of the array.

def sorr(arr):
    if len(arr) <= 1:
        return arr
    else:
        begin = sorr([i for i in arr[1:] if i<arr[0]])
        pivot = [arr[0]]
        end = sorr([i for i in arr[1:] if i >= arr[0]])
        return begin + pivot + end
        
        
