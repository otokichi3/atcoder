#!/usr/bin/env python3
# 1.入力
n = int(input())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))

# 2.美味しさの降順ソート
l = sorted(l, key=lambda x: x[1], reverse=True)

# 3.2つを選ぶ
first = l[0]
second = l[1]
ans = 0
if first[0] != second[0]:
    ans = first[1] + second[1]
else:
    ans = first[1] + second[1] // 2

for x in l[2:]:
    if first[0] != x[0] and (first[1] + x[1] > ans):
        ans = first[1] + x[1]
        break
    if first[0] == x[0] and (first[1] + x[1] // 2 > ans):
        ans = first[1] + x[1] // 2
        break

print(ans)
