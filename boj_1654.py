import sys

K, N = map(int, sys.stdin.readline().split())
lan_cables = [int(sys.stdin.readline()) for _ in range(K)]
start, end = 1, max(lan_cables)

while start <= end:
    mid = (start + end) // 2
    lines = 0

    # calculate the number of cables cut based on 'mid'
    for i in lan_cables:
        lines += i // mid

    '''
    1   2   ...     ...     max(lan)
    ^            ^               ^
    start       mid             end
    
    if lines >= N
    1   2   ...     ...     max(lan)
    ^            ^   ^            ^
               mid start           end
    else
    1   2   ...     ...     max(lan)
    ^            ^   ^            ^
    start       end mid           
    '''
    # compare the obtained value with N
    if lines >= N:
        start = mid + 1 # update start value
    else:
        end = mid - 1 # update end value

print(end)
