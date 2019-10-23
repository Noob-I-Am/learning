"""
冒泡排序

1. 遍历列表，对其中每一对相邻的两个元素进行比较，若第一个比第二个大就进行交换。

2.通过第一步将最大的元素交换到列表末尾，然后排除该元素，对前面的所有元素进行第1步操作。

3.重复进行前面两步操作。
"""


def bubbleSort(lis):
    if len(lis) <= 1:
        return lis
    unsorted = len(lis) - 1
    for _ in range(len(lis)-1):
        for i in range(unsorted):
            if lis[i] > lis[i+1]:
                lis[i], lis[i+1] = lis[i+1], lis[i]
        unsorted -= 1
        print(lis)
    return lis


a = [5, 7, 3, 4, 1, 9, 8, 2]
print('最终结果:', bubbleSort(a))


