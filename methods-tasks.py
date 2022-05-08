def func():
    print("Create a function with default argument - ")
    print("This is a function. \n")


def variable(*args):
    lst = [i for i in args]
    print("Create a function with variable length of arguments - ")

    return sum(lst)


def calculation(a, b):
    sm = a + b
    diff = a - b
    print("Return multiple values from a function - ")

    return sm, diff


if __name__ == "__main__":
    func()
    print("Sum - ", variable(20, 40))
    print(calculation(50, 30))
