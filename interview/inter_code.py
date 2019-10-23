def reverse( x: int) -> int:
    res = -1 if x < 0 else 1
    res *= int(str(abs(x))[::-1])
    if -2 ** 31 <= res <= 2 ** 31:
        return 0
    else:
        return res

print(reverse(1534236400))
