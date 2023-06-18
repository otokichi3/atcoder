from math import floor
N = int(input())
if N <= 10**3 - 1:
    print(N)
elif 10**3 <= N <= 10**4 - 1:
    print(floor(N/(10**1))*10**1)
elif 10**4 <= N <= 10**5 - 1:
    print(floor(N/(10**2))*10**2)
elif 10**5 <= N <= 10**6 - 1:
    print(floor(N/(10**3))*10**3)
elif 10**6 <= N <= 10**7 - 1:
    print(floor(N/(10**4))*10**4)
elif 10**7 <= N <= 10**8 - 1:
    print(floor(N/(10**5))*10**5)
elif 10**8 <= N <= 10**9 - 1:
    print(floor(N/(10**6))*10**6)
