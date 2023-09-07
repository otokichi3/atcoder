# 順列の生成
def make_perm():
    perm = []
    for a in range(1, 5):
        perm.append(a)
        for b in range(1, 5):
            if b in perm:
                continue
            perm.append(b)
            for c in range(1, 5):
                if c in perm:
                    continue
                perm.append(c)
                for d in range(1, 5):
                    if d in perm:
                        continue
                    perm.append(d)
                    print(perm)
                    perm.pop()
                perm.pop()
            perm.pop()
        perm.pop()


def make_perm_recursive(perm, n, m=0):
    if n == m:
        print(perm)
    else:
        for x in range(1, n + 1):
            if x in perm:
                continue
            perm.append(x)
            make_perm_recursive(perm, n, m + 1)
            perm.pop()


if __name__ == "__main__":
    # make_perm()
    make_perm_recursive([], 4)
