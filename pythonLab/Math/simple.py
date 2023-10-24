def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def sub(a, b):
    return a - b

def div(a, b):
    return a // b


# test code
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(add(a, b))
    print(mul(a, b))
    print(sub(a, b))
    print(div(a, b))
