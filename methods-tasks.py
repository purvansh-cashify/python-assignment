def func():
    print("Create a function with default argument - ")
    print("This is a function. \n")

def variable(*args):
    lst = [i for i in args]
    print("Create a function with variable length of arguments - ")

    return sum(lst)


if __name__ == "__main__":
    func()
    print("Sum - ", variable(20, 40))
