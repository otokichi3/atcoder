H = 5
W = 4
g = [
    [3, 4, 1, 6], # 14
    [2, 1, 0, 1], # 4
    [2, 1, 2, 3], # 8
    [2, 0, 1, 2], # 5
    [4, 2, 0, 3], # 9
    #13 8  4  15    40
]

sum_row = [0] * H
sum_col = [0] * W
for i in range(H):
    for j in range(W):
        sum_row[i] += g[i][j]
        sum_col[j] += g[i][j]

for i in range(H):
    print("+".join(list(map(str,g[i]))) + "=" + str(sum_row[i]))
# 3+4+1+6=14
# 2+1+0+1=4
# 2+1+2+3=8
# 2+0+1+2=5
# 4+2+0+3=9

t = list(zip(*g))
for i in range(W):
    print("+".join(list(map(str,t[i]))) + "=" + str(sum_col[i]))
# 3+2+2+2+4=13
# 4+1+1+0+2=8
# 1+0+2+1+0=4
# 6+1+3+2+3=15

print(sum(sum_row))
# 40