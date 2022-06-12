import random

from timeit import default_timer as timer


def partition(arr, p, r):
    x = arr[r]
    i = p
    for j in range(p, r):
        if arr[j] <= x:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i


def qsort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        qsort(arr, p, q-1)
        qsort(arr, q+1, r)


def quick_sort(arr):
    qsort(arr, 0, len(arr)-1)


def test(A):
    for i in range(1, len(A)):
        if A[i-1] > A[i]:
            return False
    return True


x = random.sample(range(10000), 100)
start = timer()
quick_sort(x)

print(timer() - start)
print(x)
print(test(x))
