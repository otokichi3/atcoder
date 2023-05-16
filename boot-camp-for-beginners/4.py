import math
N = int(input())
x = N / 1.08
c = int(math.ceil(x))
f = int(math.floor(x))
if int(c * 1.08) == N:
    print(c)
elif int(f * 1.08) == N:
    print(f)
else:
    print(':(')