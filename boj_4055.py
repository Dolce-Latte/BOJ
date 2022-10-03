import sys

day = 0
while True:
    p = int(sys.stdin.readline().strip())

    if p == 0:
        break
    day += 1
    time = []
    for _ in range(p):
        s, e = map(int, sys.stdin.readline().split())
        time.append((s, e))

    time.sort()

    start = 0
    answer = 0

    for half in range(33):
        t = 8 + half * 0.5
        if start >= len(time):
            break

        j = start
        min = 25
        minStart = j
        while j < len(time):
            x = time[j]
            if x[0] > t:
                break
            if t < x[1] < min:
                minStart = j
                min = x[1]
            j += 1

        if min < 25:
            answer += 1
            tt = time[minStart]
            time.remove(tt)

    print("On day {} Emma can attend as many as {} parties".format(day, answer))
