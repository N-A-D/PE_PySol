from functions import lcm

def smallest_multiple(limit):
    x = 1
    for i in range(2, limit + 1):
        x = lcm(x, i)
    return x

if __name__ == "__main__":
    print(smallest_multiple(20))