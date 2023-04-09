A, B = map(int, input().split())
count = 0
while(A != B):
    if A > B:
        count += A // B
        A = A - B * (A // B)
    else:
        count += B // A
        B = B - A * (B // A)
    if A == 1:
        count += B - 1
        break
    if B == 1:
        count += A - 1
        break
print(count)