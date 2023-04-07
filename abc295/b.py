R, C = map(int, input().split())
board = []
for i in range(R):
    board.append(list(input()))

# debug: print before
# print("[before]")
# for i in range(R):
#     print(board[i])
# print("[before]")

# solve
for i in range(R):
    for j in range(C):
        if board[i][j].isdecimal():
            # explode
            for l in range(R):
                for m in range(C):
                    kyori = abs(l - i) + abs(m - j)
                    if (
                        not (i == l and j == m)
                        and kyori <= int(board[i][j])
                        and not (board[l][m].isdecimal())
                    ):
                        board[l][m] = "."
            board[i][j] = "."
# answer
for i in range(R):
    for j in range(C):
        print(board[i][j], end="")
    print("")
