N = int(input())
S = input()
ans, d = [], 0
for c in S:
    if c == "(":
        d += 1
        ans.append(c)
    elif c == ")":
        if d > 0:
            while True:
                p = ans.pop()
                if p == "(":
                    break
            d -= 1
        else:
            ans.append(c)
    else:
        ans.append(c)
print("".join(ans))
