N = int(input())
A = list(map(int, input().split()))
num = {}
for i in range(1, N+1):
   num[i] = False 
cnt = 0
for a in A:
    if a in num:
        if num[a] == False:
            num[a] = -1
        elif num[a] == -1:
            num[a] = cnt
        elif num[a] > 0:
            pass
    cnt += 1
sorted_items = sorted(num.items(), key=lambda x:x[1])
ans = []
for i in sorted_items:
    ans.append(str(i[0]))
print(' '.join(ans))