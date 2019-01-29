def is_palindrome(w):
    l,r = 0, len(w) - 1
    while l <= r:
        if w[l] != w[r]:
            return False
        l = l + 1
        r = r - 1
    return True

def largest_palindrome_product():
    max_so_far = 0
    for i in range(100, 999):
        for j in range(100, 999):
            prod = i * j
            if prod > max_so_far and is_palindrome(str(prod)):
                max_so_far = prod
    return max_so_far
    


if __name__ == "__main__":
    print(largest_palindrome_product())