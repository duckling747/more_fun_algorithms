def binexp(a: int, b: int):
    result = 1
    while b:
        if b & 1:
            result = result * a
        a = a * a
        b = b >> 1
    return result

a = input('base: ')
b = input('exponent: ')
print(binexp(int(a), int(b)))
