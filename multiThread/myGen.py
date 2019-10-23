from collections import Iterable
def gen():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b


myGen = gen()
for i in range(1, 10):
    print(next(myGen))