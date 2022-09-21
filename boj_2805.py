import sys

n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

start, end = 0, max(trees)

while start <= end:
    mid = (start + end) // 2
    sum_of_cut_tree = 0

    for tree in trees:
        if tree > mid:
            sum_of_cut_tree += (tree - mid)

    if sum_of_cut_tree >= m:
        start = mid + 1
    else:
        end = mid - 1 +124124kl

print(end)