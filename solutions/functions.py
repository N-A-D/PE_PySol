# Computes the greatest common divisor between two numbers
def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

# Computes the lowest common multiple between two numbers
def lcm(x, y):
    return x * y // gcd(x, y)
