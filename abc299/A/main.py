#!/usr/bin/env python3
import re
 
 
def solve(N: int, S: str):
    # 文字列Sの中の*が|に挟まれていればYes
    p = '(.*\|.*\*.*\|)'
    pc = re.compile(p)
    res = re.search(pc, S)
    if res == None:
        print('out')
    else:
        print('in')