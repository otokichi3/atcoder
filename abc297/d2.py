A, B = map(int, input().split())
ans = 0
if A < B:
    A, B = B, A
while B > 0:
    ans += A // B
    A %= B
    A, B = B, A
print(ans - 1)