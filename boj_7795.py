import sys


t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    a_list = list(map(int, sys.stdin.readline().split()))
    b_list = list(map(int, sys.stdin.readline().split()))
    a_list.sort()
    b_list.sort()

    cnt = 0
    answer = 0
    for i in range(n):
        while True:
            if cnt == m or a_list[i] <= b_list[cnt]:
                answer += cnt
                break
            else:
                cnt += 1

    print(answer)

