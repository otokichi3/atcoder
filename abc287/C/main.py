#!/usr/bin/env python3
from collections import defaultdict

class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return "\n".join(f"{r}: {m}" for r, m in self.all_group_members().items())

n, m = map(int, input().split())
g = [[] * m for _ in range(n)]

uf = UnionFind(n)
for _ in range(m):
    v1, v2 = map(int, input().split())
    v1 -= 1
    v2 -= 1
    uf.union(v1, v2)
    g[v1].append(v2)
    g[v2].append(v1)

# 条件1:辺の数はN-1本
if m != n - 1:
    print("No")
    exit()

# 条件2:すべての頂点の次数が2以下
for i in range(n):
    if len(g[i]) > 2:
        print("No")
        exit()

# 条件3:連結である
if uf.group_count() > 1:
    print("No")
    exit()

print("Yes")
