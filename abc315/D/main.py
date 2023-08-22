#!/usr/bin/env python3
from pprint import pprint

h, w = map(int, input().split())
c = [list(input()) for _ in range(h)]
a = [[0] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        a[i][j] = ord(c[i][j]) - ord("a")

m = 26
row = [[0] * m for _ in range(h)]
col = [[0] * m for _ in range(w)]
for i in range(h):
    for j in range(w):
        row[i][a[i][j]] += 1
        col[j][a[i][j]] += 1
row_deleted = [False] * h
col_deleted = [False] * w


def to_delete(x):
    tot, k = 0, 0
    for j in range(m):
        tot += x[j]
        if x[j]:
            k += 1
    return tot >= 2 and k == 1

def delete(i, j):
    if row_deleted[i] or col_deleted[j]:
        return
    row[i][a[i][j]] -= 1
    col[j][a[i][j]] -= 1


upd = True
while upd:
    upd = False
    del_row = []
    del_col = []
    for i in range(h):
        if row_deleted[i]:
            continue
        if to_delete(row[i]):
            del_row.append(i)
    for j in range(w):
        if col_deleted[j]:
            continue
        if to_delete(col[j]):
            del_col.append(j)
    for i in del_row:
        for j in range(w):
            delete(i, j)
        row_deleted[i] = True
        upd = True
    for j in del_col:
        for i in range(h):
            delete(i, j)
        col_deleted[j] = True
        upd = True

ans = 0
for i in range(h):
    for j in range(w):
        if row_deleted[i] or col_deleted[j]:
            continue
        ans += 1
print(ans)
