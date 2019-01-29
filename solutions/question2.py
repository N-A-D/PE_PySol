def sum_even_terms():
    a = 1
    b = 2
    terms = []
    terms.append(b)
    while b <= 4000000:
        a, b = b, a + b
        if b % 2 == 0:
            terms.append(b)
    sum = 0
    for term in terms:
        sum = sum + term
    return sum

if __name__ == "__main__":
    print(sum_even_terms())