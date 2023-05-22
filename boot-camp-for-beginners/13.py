A, B, C = list(map(int, input().split()))
ans = 0
while A % 2 == 0 and B % 2 == 0 and C % 2 == 0:
    if A == B and B == C:
        ans = -1
        break
    a = A + B // 2 + C // 2
    b = B + A // 2 + C // 2
    c = C + A // 2 + B // 2
    A = a
    B = b
    C = c
    ans += 1
print(ans)
