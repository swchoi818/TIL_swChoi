# def MenOfPassion(A, n):
#     sum = 0
#     for i in range(1, n):
#         sum += A[i] # 코드1
#     return sum
# n = int(input())
# print(n,"\n1")

# n = int(input())
# print(n**2,"\n2")

# n = int(input())
# print(int(n*(n-1)/2),"\n2")
def MenOfPassion(n) :
    count = 0
    for i in range(1, n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                count += 1; # 코드1
    return count


print(MenOfPassion(int(input())),"\n3")

# (n-2)(n-1) *n//6