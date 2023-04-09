S = input()
# 偶奇が異なる＝位置の差が奇数
p1 = (S.rfind('B') - S.find('B')) % 2 == 1
# Kは2つのRの間にある
p2 = S.find('R') < S.find('K') < S.rfind('R')

if p1 == True and p2 == True:
    print('Yes')
else:
    print('No')