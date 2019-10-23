"""
回文检查
"""

from data_structure.Deque import Deque

def palchecker(string):
    if len(string) < 2:
        return True
    deque = Deque()
    for i in string:
        deque.addFront(i)
    while deque.size() >= 2:
        if deque.removeFront() != deque.removeRear():
            return False
        else:
            continue

    return True


print(palchecker('1221'))