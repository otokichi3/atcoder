S = list(input())


# 文字列Sが回文かどうか
def is_palindrome(s: list) -> bool:
    n = len(s)
    for i in range(n):
        if s[i] != s[n - i - 1]:
            return False
    return True


# 文字列Sに回文が含まれるかどうか
# 連続する2文字以上の文字列が回文であれば真
def include_palindrome(s: list) -> bool:
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n):
            if is_palindrome(s[i : j + 1]):
                return True
    return False


# 文字列Sの中の最長の回文を探す
def longest_palindrome(s: list) -> int:
    n = len(s)
    ans = 1
    for i in range(n):
        for j in range(i + 1, n):
            if is_palindrome(s[i : j + 1]):
                ans = max(ans, j - i + 1)
    return ans


print(f"is_palindrome: {is_palindrome(S)}")
print(f"include_palindrome: {include_palindrome(S)}")
print(f"longest_palindrome: {longest_palindrome(S)}")
