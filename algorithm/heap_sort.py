def heapify(arr, k, n):
    largest = k
    left = 2*k + 1
    right = 2*k + 2
    if (left < n) and (arr[left] > arr[largest]):
        largest = left
    if (right < n) and (arr[right] > arr[largest]):
        largest = right
    if largest != k:
        arr[k], arr[largest] = arr[largest], arr[k]
        heapify(arr, largest, n)


def build_heap(arr):
    n = len(arr)
    for i in range((n//2) - 1, 0, -1):
        heapify(arr, i, n)


def heap_sort(arr):
    build_heap(arr)
    for i in range(len(arr)-1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)


arr = [5, 3, 2, 1, 4]

heap_sort(arr)

print(arr)
