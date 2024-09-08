from collections import Counter


def find_frequency(arr):
    return Counter(arr)


arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(find_frequency(arr))
