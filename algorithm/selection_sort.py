# 가장 작은 수 부터 정렬되는 방식
def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# 가장 큰 수 부터 정렬되는 방식


def selection_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        max_idx = 0
        for j in range(1, i+1):
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    return arr


li = [5, 3, 2, 1, 4]

print(selection_sort(li))
