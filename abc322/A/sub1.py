#!/usr/bin/env python3
N = int(input())
S = input()
import re
m = re.search("ABC", S)
if m:
    print(m.start()+1)
else:
    print(-1)