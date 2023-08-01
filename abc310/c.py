N = int(input())
S = {}
for _ in range(N):
    i = input()
    ri = i[::-1]
    if i in S or ri in S:
        continue
    S[i] = False
print(len(S))