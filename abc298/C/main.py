#!/usr/bin/env python3

def main():
    N = int(input())
    Q = int(input())

    # init box
    box = {}
    for i in range(N):
        box[i + 1] = []

    # init numbers
    numbers = {}

    ans = ''
    for i in range(Q):
        query = input().split()
        # q1
        if query[0] == "1":
            box[int(query[2])].append(query[1])
        # q2
        elif query[0] == "2":
            res = sorted(box[int(query[1])])
            ans += ' '.join(res) + '\n'
        # q3
        else:
            box_list = []
            for j in range(1, N+1):
                if query[1] in box[j]:
                    box_list.append(str(j))
            ans += ' '.join(box_list) + '\n'
    print(ans)

if __name__ == '__main__':
    main()
