import sys

n = int(sys.stdin.readline())

arr = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    arr.append((y, x))


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for elem in arr:
        if elem < pivot:
            lesser_arr.append(elem)
        elif elem > pivot:
            greater_arr.append(elem)
        else:
            equal_arr.append(elem)

    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)


arr = quick_sort(arr)
for elem in arr:
    print(elem[1], elem[0])