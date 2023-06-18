N = int(input())
A = list(map(int, input().split()))
Q = int(input())
lr = [list(map(int, input().split())) for _ in range(Q)]
t = [0]
cnt = 0
for i in range(1, N):
    for j in range(A[i-1], A[i]):
        # 奇数～偶数間は起きているためスキップ
        if i % 2 == 1:
            pass
        else:
            cnt += 1
        t.append(cnt)
for q in lr:
    l, r = q
    print(t[r]-t[l])