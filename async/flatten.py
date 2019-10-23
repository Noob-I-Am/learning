"""
递归遍历所有可迭代对象使之扁平化
"""


def flatten(iter):
    for obj in iter:
        if hasattr(obj,'__iter__') and not isinstance(obj, str):
            yield from flatten(obj)
        else:
            yield (obj)


l1 = [1, 2, [3, 4], [5, [6, [7, 8, 9]]], 10, (11, 12)]
print(l1, '\n flatten to ', list(flatten(l1)))
print()
s = {'red', 'blue', 'green'}
l2 = [1, 2, (4.5, 5), range(22, 27), 'abcd', s]
print(l2, '\n flatten to ', list(flatten(l2)))