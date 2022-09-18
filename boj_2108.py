import sys
import statistics
n = int(sys.stdin.readline())

nums = []
for _ in range(n):
    nums.append(int(sys.stdin.readline()))
nums.sort()

freq = {}
for elem in nums:
    if elem in freq:
        freq[elem] += 1
    else:
        freq[elem] = 1

max_val = max(freq.values())
max_freq = []
for elem in freq:
    if freq[elem] == max_val:
        max_freq.append(elem)
if len(max_freq) > 1:
    second_freq = max_freq[1]
else:
    second_freq = max_freq[0]

arithmatic_mean = statistics.mean(nums)
print(round(arithmatic_mean))
print(nums[n//2])
print(second_freq)
print(max(nums) - min(nums))
