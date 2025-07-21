#print("         ,r\'\"7\nr`-_   ,'  ,/\n \\. \". L_r'\n   `~\\/\n      |\n      |")

# piece_cnt = [1, 1, 2, 2, 2, 8]

# piece = list(map(int, input().split()))

# for i in piece_cnt:

def isPrime(n):
    cnt = 0
    if n == 2:
        return True
    if (n != 2 and n%2 == 0) or n == 1:
        return False
    for i in range(n//3, 0, -1):
        if n%i == 0:
            cnt += 1
    if cnt > 1:
        return False
    else:
        return True

T = int(input())
even_num = []
for tc in range(T):
    even_num.append(int(input()))

result = []
count = 0

for n in range(T):
    a = int(even_num[n]/2)
    for i in range(a, 0, -1):
        if isPrime(i):
            if isPrime(even_num[n] - i):
                count += 1
    result.append(count)
    count = 0
print(*result,sep='\n')
    
    

