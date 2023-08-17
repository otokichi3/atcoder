#!/usr/bin/env python3

# 1.入力
n = int(input())
s = list(input())
q = int(input())
last = [0, 0]  # [2or3,i]
lastt2 = -1
lastt3 = -1
t, x, c = [], [], []
for i in range(q):
    a, b, c2 = input().split()
    t.append(a)
    x.append(int(b)-1)
    c.append(c2)
    # 最終全体操作の記録
    if a == "2" and lastt2 < i:
        lastt2 = i
    if a == "3" and lastt3 < i:
        lastt3 = i


# 2.最終全体操作の整理
if lastt2 == -1 and lastt3 == -1:
    last = [0, 0]
elif lastt2 > lastt3:
    last = [2, lastt2]
else:
    last = [3, lastt3]

# 3.前半の個別変更を適用
for i in range(0, last[1]):
    if t[i] == "1":
        s[x[i]] = c[i]

# 4.全体変更を適用
if last[0] == 2:
    s = list("".join(s).lower())
if last[0] == 3:
    s = list("".join(s).upper())

# 5.後半の個別変更を適用
for i in range(last[1], q):
    if t[i] == "1":
        s[x[i]] = c[i]

print("".join(s))
