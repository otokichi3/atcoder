A = []
A.append(list(map(int, input().split())))
A.append(list(map(int, input().split())))
A.append(list(map(int, input().split())))

def f():
    return \
        (A[0][0] == A[0][1] and A[0][1] == A[0][2]) or \
        (A[1][0] == A[1][1] and A[1][1] == A[1][2]) or \
        (A[2][0] == A[2][1] and A[2][1] == A[2][2]) or \
        (A[0][0] == A[1][0] and A[1][0] == A[2][0]) or \
        (A[0][1] == A[1][1] and A[1][1] == A[2][1]) or \
        (A[0][2] == A[1][2] and A[1][2] == A[2][2]) or \
        (A[0][0] == A[1][1] and A[1][1] == A[2][2]) or \
        (A[0][2] == A[1][1] and A[1][1] == A[2][0])

res = False
N = int(input())
for _ in range(N):
    b = int(input())
    for i in range(3):
        for j in range(3):
            if A[i][j] == b:
                A[i][j] = True
                if f() and not res:
                    res = True
if res:
    print('Yes')
else:
    print('No')