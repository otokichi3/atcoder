import copy

N = int(input())
A = [list(input()) for _ in range(N)]
B = copy.deepcopy(A)
for i in range(N):
    for j in range(N):
        # 最初の行
        if i == 0:
            if j == 0:
                B[i][j] = A[i + 1][j]
            else:
                B[i][j] = A[i][j - 1]

        # 最後の行
        elif i == N - 1:
            if j == N - 1:
                B[i][j] = A[i-1][j]
            else:
                B[i][j] = A[i][j + 1]

        # それ以外の行
        else:
            # 左端の列
            if j == 0:
                B[i][j] = A[i + 1][j]
            if j == N - 1:
                B[i][j] = A[i - 1][j]

for i in range(N):
    print("".join(B[i]))
