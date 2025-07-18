# n = int(input())
# score = list(map(int, input().split()))
# score.sort()
# print(score[len(score)//2])

# p = {"A" : 0, "B" : 0}
# p["A"], p["B"] = list(map(int,input().split()))
# if (p["A"] == 1 and p["B"] == 2) or (p["A"] == 2 and p["B"] == 3) or (p["A"] == 3 and p["B"] == 1):
#     print("B")
# else:
#     print("A")

# def kill_flies(m, x, y, grid, n, dir):
#     sum = grid[x][y]
#     for dx, dy in dir:
#         for i in range(1, m):
#             nx = x + dx * i
#             ny = y + dy * i
#             if 0 <= nx < n and 0 <= ny < n:
#                 sum += grid[nx][ny]
#     return sum
#     # sum = 0
#     # for i in range(1, m * 2):
#     #     a = (x - m) + i
#     #     if 0 <= a < n:
#     #         sum += grid[a][y]
#     # for i in range(1, m * 2):
#     #     a = (y - m) + i
#     #     if 0 <= a < n:
#     #         sum += grid[x][a]
    
#     # sum = sum - grid[x][y]
#     # if max < sum:
#     #     max = sum

#     # sum = 0
#     # for i in range(1, m * 2):        
#     #     a = (x - m) + i
#     #     b = (y - m) + i
#     #     if 0 <= a < n and 0 <= b < n:
#     #         sum += grid[a][b]
#     # for i in range(1, m * 2):
#     #     a = (x - m) + i
#     #     b = (y - m) - i
#     #     if 0 <= a < n and 0 <= b < n:
#     #         sum += grid[a][b]
    
#     # sum = sum - grid[x][y]
#     # if max < sum:
#     #     max = sum
    
#     # return max
    
# plus_dir = [(0, 1),(1, 0),(0, -1),(-1, 0)]
# cross_dir = [(1, 1), (-1, 1), (-1, -1), (1, -1)]
# T = int(input())
# n = [0 for _ in range(T)]
# m = [0 for _ in range(T)]
# grid = [[] for _ in range(T)]
# for test_case in range(T):
#     n[test_case], m[test_case] = map(int,input().split())
#     grid[test_case] = [0 for _ in range(n[test_case])]
#     for i in range(0, n[test_case]):
#         grid[test_case][i] = list(map(int, input().split()))
    
# for t in range(T):
#     result = 0
#     for i in range(n[t]):
#         for j in range(n[t]):
#             result = max(result, kill_flies(m[t], i, j, grid[t], n[t], plus_dir), kill_flies(m[t], i, j, grid[t], n[t], cross_dir))
        
#     print(f"#{t + 1} {result}")


# T = int(input())
# length = [0 for _ in range(T)]
# a = [0 for _ in range(T)]
# b = [0 for _ in range(T)]
# for test_case in range(T):
#     length[test_case] = list(map(int, input().split()))
#     a[test_case] = list(map(int, input().split()))
#     b[test_case] = list(map(int, input().split()))

# for t in range(T):
#     sum = 0
#     max = 0

#     if length[t][0] <= length[t][1]:
#         for j in range(length[t][1] - length[t][0] + 1):
#             for i in range(length[t][0]):
#                 sum += a[t][i] * b[t][i + j]
#             if max < sum :
#                 max = sum
#             sum = 0
#     else:
#         for j in range(length[t][0] - length[t][1] + 1):
#             for i in range(length[t][1]):
#                 sum += a[t][i + j] * b[t][i]
#             if max < sum :
#                 max = sum
#             sum = 0

#     print(f"#{t + 1} {max}")

def turnArray(array, size):
    result = [[0 for _ in range(size)] for _ in range(size)]
        
    for i in range(size):
        for j in range(size):
            result[i][j] = (array[size - j - 1][i])
    
    return result

T = int(input())
grid = [[] for _ in range(T)]
n = [0 for _ in range(T)]
for test_case in range(T):
    n[test_case] = int(input())
    grid[test_case] = [0 for _ in range(n[test_case])]
    for i in range(0, n[test_case]):
        grid[test_case][i] = list(map(int, input().split()))
    
for t in range(T):
    result = {'90': [[]], '180': [[]], '270': [[]]}
    result['90'] = turnArray(grid[t], n[t])
    result['180'] = turnArray(result['90'], n[t])
    result['270'] = turnArray(result['180'], n[t])
    print(f"#{t + 1}")
    for i in range(n[t]):
        print("".join(map(str, result['90'][i])), "".join(map(str, result['180'][i])), "".join(map(str, result['270'][i])))