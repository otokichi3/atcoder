N = int(input())
W = input().split()

words = ["and", "not", "that", "the", "you"]

for i in range(N):
  if W[i] in words:
    print('Yes')
    break
else:
  print('No')