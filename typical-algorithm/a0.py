def binsearch(a, k):
    left = 0
    right = len(a) - 1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == k:
            return mid
        elif a[mid] < k:
            left = mid +1
        else:  # a[mid] <= k
            right = mid - 1
    return -1

a = [1, 2, 3, 5, 6, 11, 13]
k = 3

result = binsearch(a, k)
print(result)
