import math
def prime_factorize_maxed(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return max(a)

def isprime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0: return False
    return True

flag = False
N, M = list(map(int, input().split()))
if N < math.sqrt(M):
    print(-1)
elif prime_factorize_maxed(M) > N:
    print(-1)
else:
    while(1):
        if isprime(M):
            M += 1
        else:
            print(M)
            break
