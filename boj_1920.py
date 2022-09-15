import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
MA = list(map(int, sys.stdin.readline().split()))


def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if key == arr[mid]:
            print(1)
            return 1
        elif key < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    print(0)
    return 0


A.sort()
for elem in MA:
    binary_search(A, elem)

