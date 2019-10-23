"""
二分查找
"""


def binary_search(lis, item):
    low = 0
    high = len(lis) - 1

    if lis[0] > item or lis[high] < item:
        return None

    while low <= high:
        mid = int(high + low/2)
        if item == lis[mid]:
            return mid
        elif item < lis[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return None


lis = list(range(1, 101))
item = 101
print(binary_search(lis, item))
