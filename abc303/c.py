N, M, H, K = list(map(int, input().split()))
S = list(input())
a = {}
for x in range(M):
    i = "".join(input().split())
    a[i] = True
chokudai = [0, 0]
for s in S:
    H -= 1
    if H == -1:
        print("No")
        exit()
    if s == "U":
        chokudai = [chokudai[0], chokudai[1] + 1]
    if s == "D":                            
        chokudai = [chokudai[0], chokudai[1] - 1]
    if s == "R":
        chokudai = [chokudai[0] + 1, chokudai[1]]
    if s == "L":               
        chokudai = [chokudai[0] - 1, chokudai[1]]
    # アイテムがあって体力がK未満のときはアイテムを使用する
    str_chokudai = "{}{}".format(str(chokudai[0]), str(chokudai[-1]))
    if str_chokudai in a and H < K:
        if a[str_chokudai]:
            H = K
            # 消費 = その座標のアイテムは次回以降使えない
            a[str_chokudai] = False
print("Yes")
