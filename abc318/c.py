n, d, p = map(int, input().split())
F = list(map(int, input().split()))
F = sorted(F, reverse=True)
ma = 0
# 周遊パスを買う枚数を計算
shuyu_cnt = 0
for i in range(0, n, d):
    s = 0
    for j in range(d):
        if i + j < n:
            s += F[i + j]
    if s > p:
        shuyu_cnt += 1
    else:
        break

# 周遊パスを使い切った以降の運賃を足す
shuyu_day = shuyu_cnt * d
ans = shuyu_cnt * p  # 周遊パスの枚数分の金額が初期値
if shuyu_day < n:
    for i in range(shuyu_day, n):
        ans += F[i]
print(ans)
