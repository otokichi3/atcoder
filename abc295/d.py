from collections import Counter
S = list(input())
ans = 0
for i in range(0, len(S)+1):
    for j in range(i+1, len(S)+1):
        c = Counter(S[i:j])
        for v in c.values():
            if v % 2 != 0:
                break
        else:
            ans += 1
print(ans)