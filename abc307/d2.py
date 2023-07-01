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
        # 最後の左括弧までpopする
        _ = l.pop()
        while True:
            lp = ans.pop()
            if lp == "(":
                break
    else:
        ans.append(c)
print(''.join(ans))