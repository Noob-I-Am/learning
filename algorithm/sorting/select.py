"""
选择排序
1.将列表中第一个元素与其后所有元素进行比较，碰到较小的便与之交换。

2.排除第1步中选出的元素，对剩下的元素进行第1步操作。

3.重复上述操作。
"""


def selectSort(lis):
    if len(lis) <= 1:
        return lis

    max_value = max(lis)
    max_index = lis.index(max_value)
    del lis[max_index]
    return selectSort(lis) + [max_value]


a = [5, 7, 3, 4, 1, 9, 8, 2]
print(selectSort(a))




