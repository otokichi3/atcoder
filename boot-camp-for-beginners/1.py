A, B = list(map(int, input().split()))
# 分子に (分母-1) を足すと切り上げられる
# -> math.ceil を使う必要がない
print((B - 1 + A - 2) // (A - 1))
