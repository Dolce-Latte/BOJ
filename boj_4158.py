import sys
# from collections import deque
#
# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
#
#
# def solution(m, n, picture):
#     answer = [0, 0]
#     visited = [[False] * n for _ in range(m)]
#
#     def bfs(x, y):
#         count = 1
#         # 큐(Queue) 구현을 위해 deque 라이브러리 사용
#         queue = deque([(x, y)])
#         # 현재 노드를 방문 처리
#         visited[x][y] = True
#         color = picture[x][y]
#         # 큐가 빌 때까지 반복
#         while queue:
#             # 큐에서 하나의 원소를 뽑아 출력
#             x, y = queue.popleft()
#             # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
#             for i in range(4):
#                 nx, ny = x + dx[i], y + dy[i]
#                 if -1 < nx < m and -1 < ny < n:
#                     if not visited[nx][ny] and picture[nx][ny] == color:
#                         queue.append((nx, ny))
#                         visited[nx][ny] = True
#                         count += 1
#         answer[0] += 1
#         answer[1] = max(answer[1], count)
#
#     for i in range(m):
#         for j in range(n):
#             if not visited[i][j] and picture[i][j] != 0:
#                 bfs(i, j)
#     return answer
#
# m, n = map(int, sys.stdin.readline().split())
#
# picture = []
# for _ in range(m):
#     picture.append(list(map(int, sys.stdin.readline().split())))
#
# print(solution(m,n,picture))

import sys

# n, m = map(int, sys.stdin.readline().split())
# trees = list(map(int, sys.stdin.readline().split()))

p = int(sys.stdin.readline())
pc = list(map(int, sys.stdin.readline().split()))
l = int(sys.stdin.readline())
lc = list(map(int, sys.stdin.readline().split()))
dis = []
for li in lc:
    for pi in pc:
        dis.append(abs(li - pi))

start, end = 0, max(dis)

while start <= end:
    mid = (start + end) // 2
    sum_of_cut_tree = 0

    for d in dis:
        if d > mid:
            sum_of_cut_tree += (d - mid)

    if sum_of_cut_tree >= 1:
        start = mid + 1
    else:
        end = mid - 1

print(end)