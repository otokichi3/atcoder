#!/usr/bin/env python3
n, m = map(int, input().split())
s = input()

# 1. 2の最大長を取得する
lc = 0
mlc = 0
for i in range(n):
    if s[i] == '2':
        lc += 1
    elif s[i] == '1':
        pass
    else:
        lc = 0
    mlc = max(mlc, lc)

# 2. 0で分割したリストを長さで逆順ソートする
ss = s.split('0')
ll = sorted(ss, key=len, reverse=True)

# 3. 最大長のリストの無印数とロゴ数をカウントする
muji_cnt = 0
logo_cnt = 0
for c in ll[0]:
    if c == '1':
        muji_cnt += 1
    else:
        logo_cnt += 1

# 4. 必要なロゴTの数を計算する
ans = 0
if m + mlc < len(ll[0]):
    ans = len(ll[0]) - m
else:
    ans = mlc
print(ans)