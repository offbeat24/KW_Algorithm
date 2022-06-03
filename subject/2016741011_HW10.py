# 쉘 정렬 (Shell Sort)

h_n = [57, 23, 10, 4, 1]

# 오름차순 (Shell Sort - Ascending)
def insertionSort_ASC(arr, first, last, h):
    i = first + h
    while i <= last:
        val = arr[i]
        pos = i
        while pos > first and arr[pos-h] > val:
                arr[pos] = arr[pos-h]
                pos -= h
        arr[pos] = val
        i += h
        
def shellSort_ASC(arr):
    n = len(arr)
    for h in h_n :
        for i in range(0, h):
            insertionSort_ASC(arr, i, n-1, h)
    return arr
    
    
    
# 내림차순 (Shell Sort - Descending)
def insertionSort_DESC(arr, first, last, h):
    i = first + h
    while i <= last:
        val = arr[i]
        pos = i
        while pos > first and arr[pos-h] < val:
            arr[pos] = arr[pos-h]
            pos -= h
        arr[pos] = val
        i += h

def shellSort_DESC(arr):
    n = len(arr)
    for h in h_n :
        for i in range(0, h) :
            insertionSort_DESC(arr, i, n-1, h)
    return arr
    
    
    
# test
from random import randint

lst = [randint(1, 101) for i in range(100)]
print('Shell Sort(ASC) :', lst)
print('->', shellSort_ASC(lst))

print()
print()

lst = [randint(1, 101) for i in range(100)]
print('Shell Sort(DESC) :', lst)
print('->', shellSort_DESC(lst))
