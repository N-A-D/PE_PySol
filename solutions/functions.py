# Computes the greatest common divisor
def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

# Computes the lowest common divisor
def lcm(x, y):
    return x * y // gcd(x, y)
    