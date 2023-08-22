#!/usr/bin/env python3
# solution1(after contest)
s = input()
print(s.replace("a","").replace("e","").replace("i","").replace("o","").replace("u",""))

# solution2(on contest)
# s = list(input())
# ans = []
# for i in range(len(s)):
#     if s[i] == "a" or s[i] == "e" or s[i] == "i" or s[i] == "o" or s[i] == "u":
#         continue
#     else:
#         ans.append(s[i])
# print("".join(ans))
