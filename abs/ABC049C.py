S = input()

words = ['dream', 'dreamer', 'erase', 'eraser']
revwords = []
for i in range(len(words)):
	revwords.append(''.join(list(reversed(words[i]))))
rev = ''.join(list(reversed(S)))

flag = True
while flag == True:
	if len(rev) == 0:
		break
	for i in range(len(revwords)):
		if rev.startswith(revwords[i]):
			rev = rev[len(revwords[i]):]
			break
	else:
		flag = False
		break

if flag:
  print('YES')
else:
  print('NO')