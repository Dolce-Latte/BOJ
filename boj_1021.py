import sys

n, m = map(int, sys.stdin.readline().split())
pop_element = list(map(int, sys.stdin.readline().split()))

queue = [i for i in range(1, n + 1)]
answer = 0

for i in range(m):
    queue_length = len(queue)
    queue_idx = queue.index(pop_element[i])

    if queue_idx < queue_length - queue_idx:
        while True:
            if queue[0] == pop_element[i]:
                del queue[0]
                break
            else:
                queue.append(queue[0])
                del queue[0]
                answer += 1
    else:
        while True:
            if queue[0] == pop_element[i]:
                del queue[0]
                break
            else:
                queue.insert(0, queue[-1])
                del queue[-1]
                answer += 1

print(answer)
