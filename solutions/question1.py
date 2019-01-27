def find_sum(upper_bound):
    multiples = []
    for i in range(upper_bound):
        if i % 3 == 0:
            multiples.append(i)
        elif i % 5 == 0:
            multiples.append(i)
    sum = 0
    for multiple in multiples:
        sum = sum + multiple
    return sum

print(find_sum(1000))