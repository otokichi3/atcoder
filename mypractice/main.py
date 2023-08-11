from unionfind import UnionFind, UnionFindByRank

# print("---init---")
# uf = UnionFind(6)
# print(uf.parents)

# print(uf)

# print("---unite---")
# uf.unite(0,2)
# print(uf.parents)
# print(uf)

# print("---union2---")
# uf.unite(1,3)
# print(uf.parents)
# uf.unite(4,5)
# print(uf.parents)
# uf.unite(1,4)
# print(uf.parents)
# print(uf)

# print(uf.members(4))
# print(uf.roots())
# print(uf.group_count())
# print(uf.all_group_members())
# print(uf.all_group_members().values())

# ufb
# print("---ufb---")
# ufb = UnionFindBasic(5)
# ufb.unite(3, 4)
# print(ufb.parents)
# ufb.unite(2, 3)
# print(ufb.parents)
# ufb.unite(1, 2)
# print(ufb.parents)
# ufb.unite(0, 4)
# print(ufb.parents)
# [0, 1, 2, 3, 3]
# [0, 1, 2, 2, 3]
# [0, 1, 1, 2, 3]
# [0, 0, 1, 2, 3]

# print([ufb.find(i) for i in range(5)])
# ufb.find(4)
# print(ufb.parents)
# [0, 0, 0, 0, 0]

print("---ufbr---")
ufbr = UnionFindByRank(8)
print(ufbr.parents)
print(*ufbr.rank)

ufbr.unite(0, 1)
print(ufbr.parents)
print(*ufbr.rank)
ufbr.unite(2, 3)
print(ufbr.parents)
print(*ufbr.rank)
ufbr.unite(4, 5)
print(ufbr.parents)
print(*ufbr.rank)
ufbr.unite(6, 7)
print(ufbr.parents)
print(*ufbr.rank)

ufbr.unite(0, 2)
print(ufbr.parents)
print(*ufbr.rank)
ufbr.unite(4, 6)
print(ufbr.parents)
print(*ufbr.rank)

# 頂上決戦
ufbr.unite(0, 4)
print(ufbr.parents)
print(*ufbr.rank)
# rank[0]:3