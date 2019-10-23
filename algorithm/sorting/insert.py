"""
插入排序
第一个元素为有序元素，将后面的元素依次记为待插入元素，与前面的有序元素从后至前比较，然后进行插入,前面有序部分扩充直至排序完。
"""


def insertSort(lis):
    if len(lis) <= 1:
        return lis
    sorted_index = 0
    while sorted_index < len(lis) - 1:
        for _ in range(sorted_index+1, 0, -1):
            if lis[_] < lis[_-1]:
                lis[_], lis[_-1] = lis[_-1], lis[_]
            else:
                break
        sorted_index += 1
    return lis


a = [5, 7, 3, 4, 1, 9, 8, 2]
print(insertSort(a))
