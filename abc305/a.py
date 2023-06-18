N = int(input())
if N % 5 == 0:
    print(N)
elif N % 5 >= 3:
    print(N + (5 - N % 5))
else:
    print(N - (N % 5))
