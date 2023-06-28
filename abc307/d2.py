# スライスはO(k)なので間に合わない
# WA*10は不明
N = int(input())
S = input()
l = []
ans = []
for i in range(N):
    c = S[i]
    if c == '(':
        l.append(i)
        ans.append(c)
    elif c == ')' and len(l) > 0:
        lp = l.pop()
        # 最後の左括弧まで切り取る
        if i+1 < N:
            ans = ans[0:lp] + ans[i+1:]
        else:
            ans = ans[0:lp]
    else:
        ans.append(c)
    print(ans)
print(''.join(ans))