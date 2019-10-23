"""
有N阶台阶，每一步可以走1步台阶或者2步台阶，求出走到第N阶台阶的方法数。

"""


fib = lambda n: n if n <= 2 else fib(n - 1) + fib(n -2)
print(fib(1))

"""
有N阶台阶，每一步可以走1步台阶或者2步台阶...也可以走n阶，求出走到第N阶台阶的方法数。

"""
fib2 = lambda n: 1 if n < 2 else fib2(n-1) + fib2(n-2)
print(fib2(1))