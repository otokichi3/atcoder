money = 300
items = (("みかん", 100), ("りんご", 200), ("ぶどう", 300))

bag = []
total = 0
for i in range(2):
    for j in range(2):
        for k in range(2):
            if 300 >= items[0][1] * i + items[1][1] * j + items[2][1] * k:
                if i == 1:
                    bag.append(items[0][0])
                    total += items[0][1]
                if j == 1:
                    bag.append(items[1][0])
                    total += items[1][1]
                if k == 1:
                    bag.append(items[2][0])
                    total += items[2][1]
                print(total, bag)
                bag = []
                total = 0
    