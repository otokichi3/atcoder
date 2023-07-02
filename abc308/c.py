from functools import cmp_to_key

# 第一引数が小さければ負の値、大きければ正の値、等しければ0を返す
def cmp(a, b):
    # Ai/(Ai+Bi),Aj/(Aj+Bj)の比較
    # 分母を取り払って整数計算出来るよう式変形する
    # ->Ai(Aj+Bj),Aj(Ai+Bi)の比較
    # このとき計算結果は最大で10^18桁となることに注意
    # ->Python
    l = a[0] * (b[0] + b[1])
    r = b[0] * (a[0] + a[1])
    # print(a, b)
    # print(l, r)
    if l == r:
        # iは連続数であり等しいことはない
        # lとrは降順だが人の番号は昇順であることに注意
        if a[2] < b[2]:
            return 1
        else:
            return -1
    elif l > r:
        return 1
    else:
        return -1

    return 0
    
N = int(input())
res = []
for i in range(N):
    A, B = map(int, input().split())
    res.append((A, B, i+1))
# print(res)
# print(res)
l = sorted(res, key=cmp_to_key(cmp), reverse=True)
# print(l)
ans = []
for v in l:
    ans.append(v[2])
print(*ans)