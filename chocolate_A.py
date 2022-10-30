import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    r, c = map(int, sys.stdin.readline().split())
    m = min(r,c)

    w = 2 * (r*c*m - (r+c)*m*(m+1)//2 + m*(m + 1)*(2*m + 1)//6)  + r*c
    b = 0
    c += 1
    b += r * c * m-(r+c)*m*(m+1)//2+m*(m+1)*(2*m+1)//6
    r += 1
    c -= 1
    b += r * c * m-(r+c)*m*(m+1)//2+m*(m+1)*(2*m+1)//6
    print(w, b)