def main():
    # Jack B.
    print("Python syntax guide")
    variables()
    strings()
    loops()
    sum(100)
    factorial(100)
    sequences()


def variables():
    print("-----Variables-----")
    x = 7
    b = "Bob"
    print(x + 3)
    print(b * 3)
    print(type(x))
    print(type(b))


def strings():
    print("------Strings-----")
    str1 = "Can't"
    str2 = 'Dave'
    str3 = """Can use ' or " or even separate
        lines """
    print(str1)
    print(str2)
    print(str3)
    x = 42
    str4 = f"X equals {x}. Fun."
    print(str4)


def loops():
    x = 0
    for i in range(6):
        x += 1
    print(f"X is equal to {6}")

    for i in range(5):
        print(i)

def sum(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    print(total)

def factorial(n):
    total = 1
    for i in range(1, n + 1):
        total *= i
    print(total)


def sequences():
    print("------Sequences-----")
    list = [4, 5, 6, 7]
    print(list)
    list[2] = 99
    print(list)
    list.append(1000)
    print(list)
    for i in range(len(list)):
        list[i] += 10
    print(list)
    product = 1
    for i in range(len(list)):
        product *= list[i]
    print(product)


main()
