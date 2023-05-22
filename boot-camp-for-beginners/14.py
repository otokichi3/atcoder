N, K = list(map(int, input().split()))
ans = N
while True:
    if ans > ans % K:
        ans %= K
    elif ans < K and abs(ans - K) < ans:
        ans = abs(ans - K)
    else:
        break
print(ans)
