N = int(input())
t_prev = 0
x_prev = 0
y_prev = 0
for i in range(N):
    # ある時刻tとtnにおける距離がtn-t以下であれば実行可能
    # ただしtnにおける点に移動した後奇数時間が残されている場合はその場に戻り得ないため実行不可
    t, x, y = map(int, input().split())
    t_delta = t - t_prev
    kyori = abs(x - x_prev) + abs(y - y_prev)
    t_prev = t
    x_prev = x
    y_prev = y
    if t_delta == kyori:
        continue
    elif t_delta > kyori and (kyori - t_delta) % 2 == 0:
        continue
    else:
        print("No")
        break
else:
    print("Yes")