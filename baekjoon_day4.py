import sys

# n, m = map(int, sys.stdin.readline().split())

# card = list(map(int,sys.stdin.readline().split()))

# result = 0
# for i in range(n - 2):
#     for j in range(i + 1,n):
#         for k in range(j + 1,n):
#             sum = card[i] + card[j] + card[k]
#             if sum <= m:
#                result = max(result,sum)
#                if result == m:
#                    break

# print(result)

digit = sys.stdin.readline()
n = int(digit)
a = 0
result = 0
for i in range(n):
    a = i
    for j in digit:
        a += int(j)
    if n == a:
        result = a

print(result)
    