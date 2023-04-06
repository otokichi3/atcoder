N = int(input())
A = list(map(int, input().split()))
def has_odd(a):
    for i in range(len(a)):
        if a[i] % 2 != 0:
            return True
    return False

ans = 0
while(has_odd(A) == False): # 偶数しかない場合
    ans += 1
    for i in range(len(A)):
        A[i] /= 2
print(ans)