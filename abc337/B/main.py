#!/usr/bin/env python3
s = input()
import re
p = 'A+|BC*|C+|AC+|^A+B+C*'
if re.fullmatch(p, s):
    print("Yes")
else:
    print("No")