N, X = map(int, input().split())
# setは重複しない要素のコレクション
# listは文字通りリスト型（ポインタをつないだだけ）
# setはハッシュテーブル
A = set(map(int, input().split()))

for a in A:
    if a - X in A: # set のためO(1)で探索可能
        print('Yes')
        break
# breakしなかった、もしくはループに入らなかった場合にelseが実行される
else:
    print('No')