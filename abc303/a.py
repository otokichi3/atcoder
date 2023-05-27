N = int(input())
S = list(input())
T = list(input())
ans = True
for i in range(N):
    if ( S[i] == T[i] ) or ( S[i] == "1" and T[i] == "l" ) or ( S[i] == "0" and T[i] == "o" ) or ( T[i] == "1" and S[i] == "l" ) or ( T[i] == "0" and S[i] == "o" ):
        pass
    else:
        print("No")
        exit()
print("Yes")
