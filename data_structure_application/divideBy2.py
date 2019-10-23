"""
十进制转各种进制
"""
from data_structure.Stack import Stack

def divide(decNumber, base=2):

    digits = '0123456789ABCDEF'

    if decNumber < base:
        return str(decNumber)
    stack = Stack()
    while decNumber > 0:
        r = decNumber % base
        decNumber = decNumber // base
        stack.push(digits[r])

    s = ''
    while not stack.isEmpty():
        s += str(stack.pop())
    return s

print(divide(233,8))