import sys

n = int(sys.stdin.readline())

coordinates = []
for _ in range(n):
    x, y = tuple(map(int, sys.stdin.readline().split()))
    coordinates.append((x, y))


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


coordinates = quick_sort(coordinates)
for elem in coordinates:
    print(elem[0], elem[1])
