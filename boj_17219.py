import sys

n, m = map(int, sys.stdin.readline().split())

site = {}
for _ in range(n):
    domain, pw = sys.stdin.readline().split()

    if domain not in site:
        site[domain] = pw
    else:
        continue

for _ in range(m):
    domain = sys.stdin.readline().strip()

    print(site[domain])