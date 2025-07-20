area = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
def count(array, n):
    for j in range(n):
        for i in range(n):
            if array[i][j] == ".":
                cnt = 0
                for ax, ay in area :
                    nx = i - ax
                    ny = j - ay
                    if (nx < n and nx >= 0) and (ny < n and ny >= 0):
                        if array[nx][ny] == "*":
                            cnt += 1
                array[i][j] = cnt
    return array

def grounping():
    pass               

T = int(input())
mine_array = [[] for _ in range(T)]
n = [0 for _ in range(T)]
for tc in range(T):
    n[tc] = int(input())
    mine_array[tc] = [0 for _ in range(n[tc])]
    for i in range(0, n[tc]):
        mine_array[tc][i] = list(input())

for t in range(T):
    print(count(mine_array[t], n[t]))
