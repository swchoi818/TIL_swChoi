N = 1000000
isPrime = [True]*N
isPrime[0] = False
isPrime[1] = False
for i in range(2, int(N**0.5) + 1):
    if isPrime[i]:
        for j in range(i + i, N, i):
            isPrime[j] = False

factor = []

def primeFactor(a):
    if isPrime[a]:
        factor.append(a)
        return
    for i in range(2, a):
        if a%i == 0:
            factor.append(i)
            j = a//i
            if isPrime[j]:
                factor.append(j)
            else:
                primeFactor(j)
            return

n = int(input())
primeFactor(n)

print(*factor,sep="\n")
