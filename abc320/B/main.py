#!/usr/bin/env python3
# powered by https://devpixiv.hatenablog.com/entry/2014/12/22/184143
def isPalindrome(s):
    flag = True
    i = 0
    j = len(s) - 1
    while flag and i <= j:
        flag &= s[i] == s[j]
        i += 1
        j -= 1
    return flag


def longestPalindrome(s):
    res = []
    N = len(s)
    ll = 0
    for i in range(N):
        for j in range(i + 1, N+1):
            sub = s[i:j]
            if isPalindrome(sub):
                res.append(sub)
                ll = max(ll, len(sub))
    results = []
    for p in res:
        if len(p) == ll:
            results.append(p)
    return results


s = list(input())
res = longestPalindrome(s)
ans = 0
for x in res:
    ans = max(ans, len(x))
print(ans)
