for i in range(8):
    row = input()
    for j in range(8):
        if row[j] == '*':
            print('abcdefgh'[j] + str(8-i))
            break