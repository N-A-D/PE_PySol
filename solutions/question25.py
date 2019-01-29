def hundred_digit_fibonacci_number():
    a, b, = 0, 1
    idx = 1
    while len(str(b)) < 1000:
        a, b = b, a + b
        idx = idx + 1
    return idx

if __name__ == "__main__":
    print(hundred_digit_fibonacci_number())    