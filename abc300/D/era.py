import resource

def eratosthenes(N: int):
    isprime = [True] * (N + 1)
    for i in range(2, N + 1):
        if not isprime[i]:
            continue
        x = i * 2
        while x <= N:
            isprime[x] = False
            x += i
    return [i for i, x in enumerate(isprime) if i > 1 and x == True]

def main():
    res = eratosthenes(10**12)
    print(len(res))

main()
    