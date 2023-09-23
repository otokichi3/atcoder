#!/usr/bin/env python3
from itertools import permutations

# 1. 入力
M = int(input())
S = []
for _ in range(3):
    s = input()
    S.append(s + s) # 2巻分


def solve(p, d):
    """順列pと0-0までの数字dを受け取りリールをすべて止めた時間crrを返す

    Args:
        p (tuple): {0,1,2}の全順列
        d (str): 0-9の数字

    Returns:
        int: すべてのリールを止めたときの時間t(リールに存在しない値があれば10**9を返す)
    """
    # dに該当する数字がないリールが一つでもあればMAXを返す
    if any(d not in S[i] for i in range(3)):
        return 10**9
    crr = 0
    # リールを止める順番は引数pによって3通りとなる
    # 番号は0-9までの数字がdによって文字列として与えられる
    # つまり、リールの止め方6パターンと止める番号0-9の10パターンの全探索を行っている。
    for i in range(3):
        crr += S[p[i]][crr % M :].index(d) + 1 # +1するのは、次のリールは止めた位置のちょうど次の位置から止めることができるから
    return crr - 1 # 3つ目のリールを止めた後も +1 しているので -1 して帳尻を合わせる


ans = 10**9
for d in range(10):
    for p in permutations(range(3)): # p is like (0,1,2), (0,2,1),...
        ans = min(ans, solve(p, str(d)))

print(ans if ans != 10**9 else -1)
