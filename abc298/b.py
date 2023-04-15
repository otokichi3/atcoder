N = int(input())
A = [input().split() for _ in range(N)]
B = [input().split() for _ in range(N)]

print(A)
print(B)
all0 = True

# all zero 判定
for i in range(N):
    for j in range(N):
        if A[i][j] == 1:
            all0 = False
            break
    if all0 == False:
        break

# all zero の場合はYes
if all0 == True:
    print('Yes')
    exit()

def judge(a, b, N):
    for i in range(len(N)):
        for j in range(len(N)):
            if a[i][j] == 1 and b[i][j] == 0:
                return False
    return True
    
def cycle(A, N):
    for i in range(3):
        for x in zip(*A[::-1]):
            print(*x,sep=' ')
print(A)
cycle(A, N)
    
# 回転による判定