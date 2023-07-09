A, B = map(int, input().split())
if A in [1, 2, 4, 5, 7, 8]:
    if B - A == 1:
        print("Yes")
    else:
        print("No")
else:
    print("No")
