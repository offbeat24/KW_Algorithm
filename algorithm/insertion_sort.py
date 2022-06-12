def insertion_sort(arr):
    for i in range(1, len(arr)):
        loc = i-1
        new_item = arr[i]
        while loc >= 0 and new_item < arr[loc]:
            arr[loc + 1] = arr[loc]
            loc -= 1
        arr[loc+1] = new_item
    return arr


def insertion_sort(arr):
    for end in range(1, len(arr)):
        for i in range(end, 0, -1):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
    return arr


li = [5, 3, 2, 1, 4]

print(insertion_sort(li))
