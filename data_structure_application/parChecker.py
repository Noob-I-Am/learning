"""
简单括号匹配
"""
from data_structure.Stack import Stack

allow = ('{', '[', '(', ')', ']', '}')


def check(symbolString):
    stack = Stack()
    for i in symbolString:
        if i == ' ':
            continue
        if i not in allow:
            return False
        pos = allow.index(i)
        if pos < len(allow) // 2:
            stack.push(i)
        else:
            if stack.isEmpty():
                return False
            else:
                if allow.index(stack.peek()) != (len(allow) - 1 - pos):
                    return False
                else:
                    stack.pop()
    if stack.isEmpty():
        return True
    return False


if __name__ == '__main__':
    a = [
        '{ { ( [ ] [ ] ) } ( ) }',
        '[ [ { { ( ( ) ) } } ] ]',
        '[ ] [ ] [ ] ( ) { }',
        '( [ ) ]',
        '( ( ( ) ] ) )',
        '[ { ( ) ]',
    ]
    for i in a:
        print(check(i))
