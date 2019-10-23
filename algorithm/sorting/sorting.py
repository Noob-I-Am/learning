"""
排序算法
"""

lis = [3, 5, 2, 1, 4]


def quickSort(lis):
    """
    快速排序
    先定一个基准 pivot
    :param lis:
    :return:
    """
    if len(lis) < 2:
        return lis
    pivot_index = 0
    pivot = lis[pivot_index]
    less = [i for i in lis if i < pivot]
    non_less = [i for i in lis if i >= pivot and lis.index(i)!=pivot_index]
    return quickSort(less) + [pivot] + quickSort(non_less)



def insertSort(lis):
    """
    插入排序
    sorted_index 表示已排序的位置
    :param lis:
    :return:
    """
    if len(lis) < 2:
        return lis
    sorted_index = 0
    while sorted_index < len(lis):
        for _ in range(sorted_index, 0, -1):
            if lis[_-1] > lis[_]:
                temp = lis[_]
                lis[_] = lis[_-1]
                lis[_-1] = temp
            else:
                break
        sorted_index += 1
    return lis


def shellsSort(lis):
    gap = len(lis) // 2
    while gap >= 1:
        for i in range(gap, len(lis)):
            for j in range(i-gap, -1, -gap):
                if lis[j] > lis[j+gap]:
                    lis[j], lis[j+gap] = lis[j+gap], lis[j]
        gap = gap // 2
    return lis

def showshells(lis):
    gap = len(lis) // 2
    while gap >= 1:
        outer = []
        for i in range(gap, len(lis)):
            inner = []
            for j in range(i-gap, -1, -gap):
                inner.append(j)
            print('\t',inner)
            outer.append(i)
        print(outer)
        gap = gap // 2
    # return lis

def showshells2(lis):
    gap = len(lis) // 2
    while gap >= 1:
        outer = []
        for i in range(0, gap):
            inner = []
            for j in range(i, len(lis), gap):
                inner.append(j)
            print('\t',inner)
            outer.append(i)
        print(outer)
        gap = gap // 2
    # return lis

def shellsSort2(lis):
    gap = len(lis) // 2
    while gap >= 1:
        for i in range(0, gap):
            for j in range(i, len(lis), gap):
                if (j+gap) < len(lis) and lis[j] > lis[j+gap]:
                    lis[j], lis[j+gap] = lis[j+gap], lis[j]
        print('gap=', gap, lis)
        gap = gap // 2
    return lis

a = [9,1,2,5,7,4,8,6,3,5]

# print(showshells2(a))
print()
print(shellsSort2(a))