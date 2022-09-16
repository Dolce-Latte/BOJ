import sys

N = int(sys.stdin.readline())

person = []
for _ in range(N):
    age, name = sys.stdin.readline().split()
    age = int(age)
    person.append((age, name))


def quick_sort_age(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2][0]
    lesser_arr, equal_arr, greater_arr = [], [], []

    for elem in arr:
        if elem[0] < pivot:
            lesser_arr.append(elem)
        elif elem[0] == pivot:
            equal_arr.append(elem)
        else:
            greater_arr.append(elem)
    return quick_sort_age(lesser_arr) + equal_arr + quick_sort_age(greater_arr)


person = quick_sort_age(person)

for elem in person:
    age, name = elem
    print(age, name)